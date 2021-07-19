from julia import Main

from ._send import _send


def score_1_sample_n_set(el_sc, se_el1_, so=True):

    _send(el_sc, None, se_el1_, None)

    Main.so = so

    return Main.eval(
        """
        score_set(
            el_,
            sc_,
            se_el1_;
            sort = so,
        )
    """
    )
