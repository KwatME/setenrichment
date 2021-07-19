from kwat import array


def _normalize_each_sample(sc_ge_sa, me):

    if me is not None:

        if me == "log":

            sc_ge_sa = sc_ge_sa.apply(array.log)

        else:

            sc_ge_sa = sc_ge_sa.apply(array.normalize, me="-0-")

        print("Normalized each sample (method {}).".format(me))

    return sc_ge_sa
