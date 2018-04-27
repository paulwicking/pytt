from unittest import TestCase
from training_tracker import tools


class TestWorkoutDiaryTools(TestCase):
    """Tests for the helper tools."""

    def test_generate_warmup_sets(self):
        test_target_1 = 100
        test_target_2 = 150

        expected_1 = [('Warm-up set 1', 40.0),
                      ('Warm-up set 2', 50.0),
                      ]

        expected_2 = [('Warm-up set 1', 60.0),
                      ('Warm-up set 2', 75.0),
                      ]

        result_1 = tools.generate_warm_up_set_list(test_target_1)
        result_2 = tools.generate_warm_up_set_list(test_target_2)

        self.assertEqual(expected_1, result_1)
        self.assertEqual(expected_2, result_2)

    def test_five_sets_based_on_target_max(self):
        test_target_1 = 100
        test_target_2 = 150
        expected_1 = [
            {
                'Set': 1,
                'Weight': 60.0,
                'Reps': 5,
                'Total': 300.0
            },
            {
                'Set': 2,
                'Weight': 70.0,
                'Reps': 5,
                'Total': 350.0,
            },
            {
                'Set': 3,
                'Weight': 80.0,
                'Reps': 5,
                'Total': 400.0,
            },
            {
                'Set': 4,
                'Weight': 90.0,
                'Reps': 5,
                'Total': 450.0,
            },
            {
                'Set': 5,
                'Weight': 100.0,
                'Reps': 5,
                'Total': 500.0,
            },
        ]
        expected_2 = [
            {
                'Set': 1,
                'Weight': 90.0,
                'Reps': 5,
                'Total': 450.0
            },
            {
                'Set': 2,
                'Weight': 105.0,
                'Reps': 5,
                'Total': 525.0,
            },
            {
                'Set': 3,
                'Weight': 120.0,
                'Reps': 5,
                'Total': 600.0,
            },
            {
                'Set': 4,
                'Weight': 135.0,
                'Reps': 5,
                'Total': 675.0,
            },
            {
                'Set': 5,
                'Weight': 150.0,
                'Reps': 5,
                'Total': 750.0,
            },
        ]

        result_1 = tools.generate_set_list(test_target_1)
        result_2 = tools.generate_set_list(test_target_2)

        self.assertEqual(expected_1, result_1)
        self.assertEqual(expected_2, result_2)

    def test_can_sum_total_weight_in_a_list_of_sets(self):
        test_max_weight = 100
        test_set_list = tools.generate_set_list(test_max_weight)
        expected = 2000

        test_result = tools.total_weight_from_sets(test_set_list)

        self.assertEqual(expected, test_result)

    def test_pounds_to_kilogram(self):
        expected = 0.45359237
        result = tools.pounds_to_kilogram(1)

        self.assertEqual(expected, result)

    def test_kilograms_to_pounds(self):
        expected = 2.2046226218488
        result = tools.kilogram_to_pounds(1)

        self.assertEqual(expected, result)

    def test_sanitize_factor(self):
        illegal_value = 'This value is illegal'
        expected = 1.9

        result = tools.sanitize_factor(illegal_value)

        self.assertEqual(expected, result)

    def test_protein_per_meal(self):
        expected = 40
        result = tools.protein_per_meal(100)

        self.assertEqual(expected, result)

    def test_protein_per_day(self):
        expected = 190
        result = tools.protein_per_day(100)

        self.assertEqual(expected, result)
