from numpy import inf


def _select_set(
    se_fe_,
    mi,
    ma,
):

    if mi is None:

        mi = 0

    if ma is None:

        ma = inf

    se_fe_ = {se: fe_ for se, fe_ in se_fe_.items() if mi <= len(fe_) <= ma}

    print("Selected {} sets ({} <= size <= {}).".format(len(se_fe_), mi, ma))

    return se_fe_
