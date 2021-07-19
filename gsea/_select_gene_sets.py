def _select_gene_sets(
    gm,
    mi,
    ma,
):

    gm = {se: ge_ for se, ge_ in gm.items() if mi <= len(ge_) <= ma}

    print("Selected {} gene sets ({} <= size <= {}).".format(len(gm), mi, ma))

    return gm
