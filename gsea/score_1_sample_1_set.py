from julia import Main

from ._send import _send


def score_1_sample_1_set(el_sc, el1_, so=True, pl=True, title="Score Set"):

    _send(el_sc, el1_, None, None)

    Main.so = so

    Main.pl = pl

    Main.title = title

    return Main.eval(
        """
        score_set(
            el_,
            sc_,
            el1_;
            sort = so,
            plot = pl,
            title = title,
        )
    """
    )
