from . import Main
from ._send_to_julia import _send_to_julia


def score_1_n(el_sc, se_el_, we=1.0, al="ks"):

    _send_to_julia(el_sc, None, None, se_el_, we, al)

    if al in ["ks", "auc"]:

        return Main.eval(
            """
            score_set(
                el_,
                sc_,
                se_el_;
                we = we,
                al = al,
            )
        """
        )

    elif al == "js":

        return Main.eval(
            """
            score_set_new(
                el_,
                sc_,
                se_el_;
            )
        """
        )
