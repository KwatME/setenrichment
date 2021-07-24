def select_set(
    se_el_,
    mi,
    ma,
):

    se_el_ = {se: el_ for se, el_ in se_el_.items() if mi <= len(el_) <= ma}

    print("Selected {} sets ({} <= size <= {}).".format(len(se_el_), mi, ma))

    return se_el_
