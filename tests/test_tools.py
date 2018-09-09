from unittest import TestCase
from pytt import tools


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
        too_low_value = 1.0
        negative_value = -1.9
        too_high_value = 3.0

        expected_low = 1.6
        expected_high = 2.2
        expected_illegal = 1.9

        illegal_result = tools.sanitize_factor(illegal_value)
        too_low_result = tools.sanitize_factor(too_low_value)
        negative_value_result = tools.sanitize_factor(negative_value)
        too_high_result = tools.sanitize_factor(too_high_value)

        self.assertEqual(expected_illegal, illegal_result)
        self.assertEqual(expected_low, too_low_result)
        self.assertEqual(expected_low, negative_value_result)
        self.assertEqual(expected_high, too_high_result)

    def test_protein_per_meal(self):
        expected = 40
        result = tools.protein_per_meal(100)

        self.assertEqual(expected, result)

    def test_protein_per_day(self):
        expected = 190
        result = tools.protein_per_day(100)

        self.assertEqual(expected, result)

    def test_calulate_set_weight_normalizes_return_value_to_plate_size(self):
        orm = 100
        target_max = 67.5
        test_set = iter(list(range(100, 101, 10)))
        plate_size = 1.25

        deviating_test_set = iter(list(range(100, 101, 10)))
        target_max_deviating_from_plate_size = 68.5

        expected = 67.5
        result = tools.calculate_set_weight(orm, target_max, test_set, plate_size)
        result_from_deviating_weight = tools.calculate_set_weight(
            orm, target_max_deviating_from_plate_size, deviating_test_set, plate_size)

        self.assertEqual(result, expected)

        self.assertEqual(result_from_deviating_weight, expected)

    def test_can_match_weight_to_plate_size(self):
        expected = 67.5
        test_weight = 68.5
        test_plate = 1.25

        result = tools.match_weight_to_plate_size(test_weight, test_plate)

        self.assertEqual(result, expected)

    def test_plate_matching_rounds_up_when_weight_diff_is_one_plate_or_less(self):
        test_base_weight = 67.5
        test_plate = 1.25
        test_weight = test_base_weight + test_plate

        expected = test_base_weight + (2 * test_plate)
        result = tools.match_weight_to_plate_size(test_weight, test_plate)

        self.assertEqual(result, expected)

    def test_generated_sets_have_weights_matched_to_plates(self):
        expected = [
            {'Set': 1, 'Weight': 37.5, 'Reps': 5, 'Total': 187.5},
            {'Set': 2, 'Weight': 45.0, 'Reps': 5, 'Total': 225.0},
            {'Set': 3, 'Weight': 50.0, 'Reps': 5, 'Total': 250.0},
            {'Set': 4, 'Weight': 57.5, 'Reps': 5, 'Total': 287.5},
            {'Set': 5, 'Weight': 62.5, 'Reps': 5, 'Total': 312.5}
        ]
        result = tools.generate_set_list(62.5)

        self.assertEqual(result, expected)

    def test_calculate_lift_to_bodyweight_ratio(self):
        test_lift_weight = 80
        test_bodyweight = 100

        expected = 0.8
        actual = tools.lift_to_bodyweight_ratio(test_lift_weight, test_bodyweight)

        self.assertEqual(expected, actual)

    def test_lift_to_bodyweight_ratio_handles_returns_None_on_zero_values(self):
        test_lift_weight = 0
        test_body_weight = 100

        expected = None
        actual = tools.lift_to_bodyweight_ratio(test_lift_weight, test_body_weight)
        self.assertEqual(expected, actual)

        # Swap the values
        test_lift_weight = 100
        test_body_weight = 0

        actual = tools.lift_to_bodyweight_ratio(test_lift_weight, test_body_weight)
        self.assertEqual(expected, actual)

        # Both values are zero
        test_lift_weight = 0
        test_body_weight = 0

        actual = tools.lift_to_bodyweight_ratio(test_lift_weight, test_body_weight)
        self.assertEqual(expected, actual)

    def test_lift_to_bodyweight_ratio_returns_None_on_negative_values(self):
        test_lift_weight = 10
        test_body_weight = -50

        expected = None
        actual = tools.lift_to_bodyweight_ratio(test_lift_weight, test_body_weight)

        self.assertEqual(expected, actual)

    def test_calorie_to_joule_conversion(self):
        calories = 1000
        expected = 4184
        actual = tools.calorie_to_joule(calories)

        self.assertEqual(expected, actual)

        calories2 = 1750
        expected2 = 7322
        actual2 = tools.calorie_to_joule(calories2)

        self.assertEqual(expected2, actual2)
