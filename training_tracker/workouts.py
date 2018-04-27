"""
Workouts.
"""
import json


class Exercise:
    """A container for exercises."""
    pass


class Workout:
    """A workout contains exercises."""

    def __init__(self):
        self.workout_notes = ""
        self._exercises = [{'Exercise': 'Squat',
                            'Sets': [(1, 60),
                                     (2, 70),
                                     (3, 80),
                                     (4, 90),
                                     (5, 100)
                                     ],
                            'Description': 'Squats are awesome',
                            }]

    def add_exercise(self, exercise, number_of_sets, target_weight):
        """Add an exercise to this workout."""
        pass

    def exercise_list(self):
        """Returns a list of exercises for this workout."""
        return self._exercises

    def save_workout(self):
        """Stores the current workout as a json-file."""
        try:
            with open('workouts.json', 'w') as out_file:
                out_data = json.dumps(self._exercises)
                out_file.write(out_data)
        except IOError:
            raise IOError

    def load_workout(self):
        """Loads a json-file containing workout information."""
        try:
            with open('workouts.json', 'r') as in_file:
                self._exercises = json.load(in_file)
        except IOError:
            raise IOError
