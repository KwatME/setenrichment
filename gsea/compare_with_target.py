from kwat.information import get_signal_to_noise
from kwat.row import compare_with_target as row_compare_with_target
from pandas import Series


def compare_with_target(ta, da, fu, separate=True, n_jo=1):

    if fu == "signal_to_noise":

        fu = get_signal_to_noise

    elif fu == "median_difference":

        raise

    elif fu == "median_ratio":

        raise

    else:

        raise

    return Series(
        row_compare_with_target(ta, da.values, fu, separate, n_jo=n_jo),
        name=fu.__name__,
        index=da.index,
    ).sort_values()
