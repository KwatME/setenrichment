from kwat import array


def _normalize_each_sample(sc_ge_sa, me):

    if me is not None:

        if me == "log":

            sc_ge_sa = sc_ge_sa.apply(array.log)

        elif me[:4] == "rank":

            sp1, sp2 = me.split()

            sc_ge_sa = sc_ge_sa.apply(array.normalize, me=sp1, ra=sp2)

        else:

            sc_ge_sa = sc_ge_sa.apply(array.normalize, me=me)

        print("Normalized each sample (method {}).".format(me))

    return sc_ge_sa
