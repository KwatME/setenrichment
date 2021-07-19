from . import Main
from ._send import _send


def score_n_sample_n_set(sc_el_sa, se_el1_, me="classic", n_jo=1):

    _send(None, None, se_el1_, sc_el_sa.reset_index())

    Main.me = me

    Main.n_jo = n_jo

    return Main.eval(
        """
        Pandas.DataFrame(score_set(
            sc_el_sa,
            se_el1_;
            me = me,
            n_jo = n_jo,
        ))
    """
    ).set_index("Set")
