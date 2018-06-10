"""Helper functions for a workout diary application."""


def generate_set_list(target_max, sets=5, reps=5, orm=100):
    """Generate workout sets.

    :param: `target_max` Target max weight in kilo.
    :param: `sets` (`int`): Number of sets.
    :param: `reps` (int): Number of repetitions per set.
    :param: `orm`: One Repetition Max weight in percent.

    Returns a list of dictionaries containing workout sets
    """
    workout_sets = iter([sets for sets in list(range(60, 101, 10))])
    result = []

    for set_number in range(sets):
        this_set_number = set_number + 1  # We're counting from 0, add 1 so that it looks nice
        this_weight = calculate_set_weight(orm, target_max, workout_sets, plate_size=1.25)
        this_set_total = float(this_weight * reps)
        this_set = {
            'Set': this_set_number,
            'Weight': this_weight,
            'Reps': reps,
            'Total': this_set_total,
        }

        result.append(this_set)

    return result


def calculate_set_weight(orm, target_max, workout_sets, plate_size):
    """Return weight for one specific set, normalized to plate size.

    :param orm: One repetition maximum
    :param target_max:
    :param workout_sets:
    :param plate_size: The weight of a plate in kilo.
    :return:
    """

    this_weight = float(target_max * (next(workout_sets) / orm))
    if (this_weight % plate_size) > 0:
        this_weight = match_weight_to_plate_size(this_weight, plate_size)

    return this_weight


def match_weight_to_plate_size(weight, single_plate_size):
    """Return a weight that can be loaded with the available plates.

    :param weight:
    :param single_plate_size:
    :return:
    """
    pair_of_plates = single_plate_size * 2
    low_weight = weight - (weight % pair_of_plates)
    high_weight = low_weight + pair_of_plates

    if (weight % pair_of_plates) < single_plate_size:
        return low_weight
    else:
        return high_weight


def generate_warm_up_set_list(target_max, single_plate_weight=1.25):
    """Generate at list of warm-up sets for the given target max.

    Returns a list of two tuples that contain warm-up out sets at 40 % and 50 %
    of target max weight.
    """
    first_warmup_set = match_weight_to_plate_size((target_max * .4), single_plate_weight)
    second_warmup_set = match_weight_to_plate_size((target_max * .5), single_plate_weight)
    return [('Warm-up set 1', first_warmup_set),
            ('Warm-up set 2', second_warmup_set),
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

    else:
        #  Return 1.9 for all non-int or non-float values
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


def lift_to_bodyweight_ratio(lift=None, bodyweight=None):
    """Return the lift weight to body weight ratio.

    :param lift: ``int`` or ``float``. The lifted weight.
    :param bodyweight: ``int`` or ``float``, body weight.
    :return: Ratio as ``int`` or ``float``.
    """
    if not lift or not bodyweight:
        return None

    elif (lift < 0) or (bodyweight < 0):
        return None

    return lift / bodyweight
