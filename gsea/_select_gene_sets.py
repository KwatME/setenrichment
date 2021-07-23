def _select_gene_sets(
    se_ge_,
    mi,
    ma,
):

    se_ge_ = {se: ge_ for se, ge_ in se_ge_.items() if mi <= len(ge_) <= ma}

    print("Selected {} gene sets ({} <= size <= {}).".format(len(se_ge_), mi, ma))

    return se_ge_
