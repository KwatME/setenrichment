from julia import Main

from ._send import _send


def score_1_sample_1_set(
    el_sc, el1_, so=True, me="classic", pl=True, title="Score Set"
):

    _send(el_sc, el1_, None, None)

    Main.so = so

    Main.pl = pl

    Main.title = title

    if me == "classic":

        fu = "score_set"

    elif me == "new":

        fu = "score_set_new"

    return Main.eval(
        """
        {}(
            el_,
            sc_,
            el1_;
            so = so,
            pl = pl,
            title = title,
        )
    """.format(
            fu
        )
    )
