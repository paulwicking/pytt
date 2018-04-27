"""Helper functions for a workout diary application."""


def generate_set_list(target_max, sets=5, reps=5, orm=100):
    """Generate workout sets.

    Returns a list of tuples containing workout sets
    """
    workout_sets = iter([sets for sets in list(range(60, 101, 10))])
    result = []

    for set_number in range(sets):
        this_set_number = set_number + 1  # We're counting from 0, add 1 so that it looks nice
        this_weight = float(target_max * (next(workout_sets) / orm))
        this_set_total = float(this_weight * reps)
        this_set = {
            'Set': this_set_number,
            'Weight': this_weight,
            'Reps': reps,
            'Total': this_set_total,
        }

        result.append(this_set)

    return result


def generate_warm_up_set_list(target_max):
    """Generate at list of warm-up sets for the given target max.

    Returns a list of two tuples that contain warm-up out sets at 40 % and 50 %
    of target max weight.
    """
    return [('Warm-up set 1', target_max * .4),
            ('Warm-up set 2', target_max * .5),
            ]


def protein_per_meal(body_weight):
    """Returns a suggestion for grams of protein per meal based on body weight in kilogram."""
    return 0.4 * body_weight


def sanitize_factor(factor):
    """Sanitizes the protein per day factor and returns a legal value."""
    if type(factor) == int or type(factor) == float:
        if factor < 1.6:
            return 1.6
        elif factor > 2.2:
            return 2.2
        else:
            return float(factor)

    if type(factor) != float or type(factor) != int:
        return 1.9


def protein_per_day(body_weight, factor=1.9):
    """Returns grams of protein per day based on body weight and factor.

    Factor can be in the range of 1.6 - 2.2, the default value is 1.9.
    """
    sanitize_factor(factor)
    return body_weight * factor


def kilogram_to_pounds(kilogram):
    """Returns the pound equivalent of kilogram."""
    return kilogram * 2.2046226218488


def pounds_to_kilogram(pound):
    """Returns the kilogram equivalent of pound."""
    return pound * 0.45359237


def total_weight_from_sets(set_list):
    """Returns the total weight in kilo of all reps in all sets."""
    total_weight = 0
    for set_ in set_list:
        total_weight += set_['Total']

    return total_weight
