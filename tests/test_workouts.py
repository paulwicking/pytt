import json
from unittest import TestCase
from unittest.mock import patch, mock_open
from pytt.workouts import Exercise, Workout


class TestWorkouts(TestCase):
    def test_can_save_workouts(self):
        with patch('builtins.open', mock_open(read_data='data')) as mock_file:
            test_workout = Workout()
            test_workout.add_exercise("Squat", 5, 100)

            test_workout.save_workout()

            mock_file.assert_called_once_with('workouts.json', 'w')

    def test_can_load_workouts(self):
        expected = json.dumps([{"Name": "Deadlifts",
                                "Sets": [[1, 60], [2, 70], [3, 80], [4, 90], [5, 100]],
                                "Description": "Deadlifts are awesome"
                                }])
        with patch('builtins.open', mock_open(read_data=expected)) as mock_file:
            test_workout = Workout()
            test_workout.add_exercise("Squat", 5, 100)

            test_workout.load_workout()

            mock_file.assert_called_once_with('workouts.json', 'r')

    def test_save_and_load_workouts_raises_IOError_exceptions(self):
        m = mock_open()
        m.side_effect = IOError

        with patch('builtins.open', m, create=True):
                test_workout = Workout()
                with self.assertRaises(IOError):
                    test_workout.load_workout()

                with self.assertRaises(IOError):
                    test_workout.save_workout()

    def test_create_set(self):
        # squats = Exercise("Squat")
        # target_weight = 100
        # sets = 5
        # result = workouts.create_set(exercise, sets, target_weight)
        pass

    def test_can_get_list_of_exercises_from_workout(self):
        test_workout = Workout()
        test_workout.add_exercise("Squat", 5, 100)

        result = test_workout.exercise_list()

        self.assertEqual(len(result), 1)

    def test_can_add_new_exercise_to_workout(self):
        test_workout = Workout()
        test_workout.add_exercise("Squat", 5, 100)

        expected = [{'Exercise': 'Squat',
                     'Sets': [(1, 60),
                              (2, 70),
                              (3, 80),
                              (4, 90),
                              (5, 100)
                              ],
                     'Description': 'Squats are awesome',
                     }
                    ]
        result = test_workout.exercise_list()

        self.assertEqual(expected, result)

    def test_can_retrieve_a_previously_logged_workout(self):
        # TODO implement this test then redo the test to log a workout.
        pass

    def test_can_log_a_workout(self):
        test_workout = Workout()
        test_date = '28-01-2018'
        test_exercise_list = [Exercise("Test exercise 1"), Exercise("Test exercise 2")]
        test_notes = "some random note"

        test_workout.log_workout(test_date, test_exercise_list, test_notes)


class TestExercises(TestCase):
    def test_exercise_can_have_a_name(self):
        exercise_name = "Squat"
        test_exercise = Exercise(exercise_name)

        self.assertEqual(exercise_name, test_exercise.name)
