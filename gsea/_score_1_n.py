from . import Main
from ._send_to_julia import _send_to_julia


def _score_1_n(fe_sc, se_fe_, we=1.0, al="ks"):

    _send_to_julia(fe_sc, None, None, se_fe_, we, al)

    if al in ["ks", "auc"]:

        return Main.eval(
            """
            score_set(
                fe_,
                sc_,
                se_fe_;
                we = we,
                al = al,
            )
        """
        )

    elif al == "js":

        return Main.eval(
            """
            score_set_new(
                fe_,
                sc_,
                se_fe_;
            )
        """
        )
