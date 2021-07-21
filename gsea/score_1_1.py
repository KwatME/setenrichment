from . import Main
from ._send_to_julia import _send_to_julia


def score_1_1(el_sc, el1_, we=1.0, me="ks", pl=True, title="Title"):

    _send_to_julia(el_sc, el1_, None, None, we, me)

    Main.pl = pl

    Main.title = title

    if me in ["ks", "auc"]:

        return Main.eval(
            """
            score_set(
                el_,
                sc_,
                el1_;
                we = we,
                me = me,
                pl = pl,
                title = title,
            )
        """
        )

    elif me == "js":

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

    raise
