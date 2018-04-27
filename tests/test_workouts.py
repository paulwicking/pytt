import json
from unittest import TestCase
from unittest.mock import patch, mock_open
from training_tracker.workouts import Exercise, Workout


class TestWorkouts(TestCase):
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
