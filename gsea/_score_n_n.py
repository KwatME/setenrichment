from . import Main
from ._send_to_julia import _send_to_julia


def _score_n_n(sc_el_sa, se_el1_, we=1.0, me="ks", n_jo=1):

    _send_to_julia(None, None, se_el1_, sc_el_sa.reset_index())

    Main.we = we

    Main.eval(
        """
        we = Float64(we)
    """
    )

    Main.me = me

    Main.n_jo = n_jo

    return Main.eval(
        """
        Pandas.DataFrame(score_set(
            sc_el_sa,
            se_el1_;
            we = we,
            me = me,
            n_jo = n_jo,
        ))
    """
    ).set_index("Set")
