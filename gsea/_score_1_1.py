from . import Main
from ._send_to_julia import _send_to_julia


def _score_1_1(fe_sc, fe_, we=1.0, al="ks", pl=True, title="Title"):

    _send_to_julia(fe_sc, None, fe_, None, we, al)

    Main.pl = pl

    Main.title = title

    if al in ["ks", "auc"]:

        return Main.eval(
            """
            score_set(
                fe_,
                sc_,
                fe1_;
                we = we,
                al = al,
                pl = pl,
                title = title,
            )
        """
        )

    elif al == "js":

        return Main.eval(
            """
            score_set_new(
                fe_,
                sc_,
                fe1_;
                pl = pl,
                title = title,
            )
        """
        )
