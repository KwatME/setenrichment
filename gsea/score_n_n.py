from . import Main
from ._send_to_julia import _send_to_julia


def score_n_n(sc_el_sa, se_el_, we=1.0, al="ks", n_jo=1):

    _send_to_julia(None, sc_el_sa.reset_index(), None, se_el_, we, al)

    Main.n_jo = n_jo

    return Main.eval(
        """
        Pandas.DataFrame(score_set(
            sc_el_sa,
            se_el_;
            we = we,
            al = al,
            n_jo = n_jo,
        ))
    """
    ).set_index("Set")
