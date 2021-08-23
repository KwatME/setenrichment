from pandas import Series

from kwat.array_array import (
    get_cosine_distance,
    get_mean_difference,
    get_mean_ratio,
    get_median_difference,
    get_median_ratio,
    get_pearson_correlation,
    get_signal_to_noise,
)
from kwat.row import compare_with_target as row_compare_with_target


def compare_with_target(ta, da, fu, n_jo=1):

    if fu == "signal_to_noise":

        separate = True

        fu = get_signal_to_noise

    elif fu == "mean_difference":

        separate = True

        fu = get_mean_difference

    elif fu == "mean_ratio":

        separate = True

        fu = get_mean_ratio

    elif fu == "median_difference":

        separate = True

        fu = get_median_difference

    elif fu == "median_ratio":

        separate = True

        fu = get_median_ratio

    elif fu == "cosine_distance":

        separate = False

        fu = get_cosine_distance

    elif fu == "pearson_correlation":

        separate = False

        fu = get_pearson_correlation

    else:

        raise

    return Series(
        row_compare_with_target(ta, da.values, fu, separate, n_jo=n_jo),
        name=fu.__name__,
        index=da.index,
    ).sort_values()
