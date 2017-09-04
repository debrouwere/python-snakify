import unittest

from .snakify import snakify

cases = {
    'OneFineMorning': 'one_fine_morning',
    'Discounted by 20%': 'discounted_by_20',
    '23 Days of Summer': 'twenty_three_days_of_summer',
    'ratherLate': 'rather_late',
    'Flammeküche': 'flammekuche',
    'avgTimeOnPage': 'avg_time_on_page',
    'avgTimeOn12thPage': 'avg_time_on_12th_page',
}


class TestSnakify(unittest.TestCase):
    def test_snakify(self):
        for original, expected in cases.items():
            actual = snakify(original)
            self.assertEqual(actual, expected)
