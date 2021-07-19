from julia import Main

from ._send import _send


def score_1_sample_n_set(el_sc, se_el1_, so=True, me="classic"):

    _send(el_sc, None, se_el1_, None)

    Main.so = so

    if me == "classic":

        fu = "score_set"

    elif me == "new":

        fu = "score_set_new"

    return Main.eval(
        """
        {}(
            el_,
            sc_,
            se_el1_;
            so = so,
        )
    """.format(
            fu
        )
    )
