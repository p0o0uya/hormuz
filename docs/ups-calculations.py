#!/usr/bin/env python3
"""Reproduce Hormuz preliminary UPS sizing and audit the editable CSV estimates.

Run: python3 docs/ups-calculations.py [--check]
No dependencies. No files are changed. Constants are planning assumptions,
not substitutes for battery discharge curves or manufacturer protection data.
"""
import argparse
import csv
import json
import math
from pathlib import Path

LOAD_W = 50_000
AC_V = 400
LOAD_PF = 0.90
EFFICIENCY = 0.94
BLOCKS_PER_STRING = 40
CELLS_PER_BLOCK = 6
CAPACITY_AH = 50
CAPACITY_RATING_H = 20
END_V_PER_CELL = 1.75
PEUKERT_EXPONENT = 1.25
DISCHARGE_FRACTION = 0.50
AGE_FACTOR = 0.80
TEMPERATURE_FACTOR = 0.90
RUNTIME_MARGIN = 1.10
CONTINGENCY = 0.20
EXCHANGE_IRT_PER_USD = 270_000  # scenario retained from earlier site proposal


def sizing_rows():
    voltage = BLOCKS_PER_STRING * CELLS_PER_BLOCK * END_V_PER_CELL
    current = LOAD_W / (EFFICIENCY * voltage)
    reference_current = CAPACITY_AH / CAPACITY_RATING_H
    rows = []
    for minutes in (5, 10, 15, 30, 60):
        strings = math.ceil(current / reference_current *
                            (minutes * RUNTIME_MARGIN /
                             (60 * CAPACITY_RATING_H * DISCHARGE_FRACTION *
                              AGE_FACTOR * TEMPERATURE_FACTOR)) **
                            (1 / PEUKERT_EXPONENT))
        runtime = (60 * CAPACITY_RATING_H *
                   (reference_current / (current / strings)) ** PEUKERT_EXPONENT *
                   DISCHARGE_FRACTION * AGE_FACTOR * TEMPERATURE_FACTOR)
        rows.append(dict(target_minutes=minutes, design_minutes=round(minutes * RUNTIME_MARGIN, 2),
                         strings=strings, blocks_per_string=BLOCKS_PER_STRING,
                         total_batteries=strings * BLOCKS_PER_STRING,
                         nominal_kwh=round(strings * BLOCKS_PER_STRING * 12 * CAPACITY_AH / 1000, 2),
                         eod_current_per_string_a=round(current / strings, 2),
                         screening_runtime_minutes=round(runtime, 2)))
    return rows


def cost_totals(path):
    totals = {'stationary': 0, 'automotive': 0}
    with path.open(newline='', encoding='utf-8') as handle:
        for row in csv.DictReader(handle):
            value = int(row['quantity']) * int(row['unit_irt'])
            if value != int(row['line_irt']):
                raise ValueError(f"Incorrect line total: {row['item']}")
            scenarios = totals if row['scenario'] == 'common' else (row['scenario'],)
            for scenario in scenarios:
                totals[scenario] += value
    return {key: {'subtotal_irt': value,
                  'contingency_irt': round(value * CONTINGENCY),
                  'total_irt': round(value * (1 + CONTINGENCY)),
                  'usd_scenario': round(value * (1 + CONTINGENCY) / EXCHANGE_IRT_PER_USD, 2)}
            for key, value in totals.items()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Audit CSVs and proposal totals')
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    rows = sizing_rows()
    costs = cost_totals(root / 'ups-estimate.csv')
    result = dict(ac_load_current_a=round(LOAD_W / (math.sqrt(3) * AC_V * LOAD_PF), 2),
                  dc_load_power_kw=round(LOAD_W / EFFICIENCY / 1000, 3),
                  dc_eod_current_a=round(LOAD_W / (EFFICIENCY * BLOCKS_PER_STRING *
                                                   CELLS_PER_BLOCK * END_V_PER_CELL), 2),
                  sizing=rows, estimates=costs)
    if args.check:
        with (root / 'ups-battery-sizing.csv').open(newline='', encoding='utf-8') as handle:
            actual = list(csv.DictReader(handle))
        assert len(actual) == len(rows), 'Sizing row count differs'
        for expected, observed in zip(rows, actual):
            assert expected.keys() == observed.keys(), 'Sizing CSV columns differ'
            for key, value in expected.items():
                assert math.isclose(float(observed[key]), value, abs_tol=0.005), (key, observed, expected)
            assert expected['screening_runtime_minutes'] >= expected['design_minutes']
        text = (root / 'ups-proposal.md').read_text(encoding='utf-8')
        for scenario in costs.values():
            for key in ('subtotal_irt', 'contingency_irt', 'total_irt'):
                assert f"{scenario[key]:,}" in text, f'Missing proposal total: {scenario[key]}'
        assert '160 batteries' in text, 'Baseline quantity missing'
        print('PASS: sizing formulas, CSV line totals, runtime margin, and proposal totals agree.')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
