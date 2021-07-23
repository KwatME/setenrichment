from . import Main
from ._send_to_julia import _send_to_julia


def score_1_1(el_sc, el_, we=1.0, al="ks", pl=True, title="Title"):

    _send_to_julia(el_sc, None, el_, None, we, al)

    Main.pl = pl

    Main.title = title

    if al in ["ks", "auc"]:

        return Main.eval(
            """
            score_set(
                el_,
                sc_,
                el1_;
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
                el_,
                sc_,
                el1_;
                pl = pl,
                title = title,
            )
        """
        )
