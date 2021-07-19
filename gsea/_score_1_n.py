from julia import Main

from ._send_to_julia import _send_to_julia


def _score_1_n(el_sc, se_el1_, we=1.0, me="ks"):

    _send_to_julia(el_sc, None, se_el1_, None)

    Main.we = we

    Main.eval(
        """
        we = Float64(we)
    """
    )

    Main.me = me

    if me in ["ks", "auc"]:

        return Main.eval(
            """
            score_set(
                el_,
                sc_,
                se_el1_;
                we = we,
                me = me,
            )
        """
        )

    elif me == "js":

        return Main.eval(
            """
            score_set_new(
                el_,
                sc_,
                se_el1_;
            )
        """
        )

    raise
