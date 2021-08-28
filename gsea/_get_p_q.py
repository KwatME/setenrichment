from numpy import array, full, nan

from kwat.significance import get_p_value, get_q_value


def _get_p_q(se_en, se_ra_):

    pv_ = full(len(se_en), nan)

    for ie, (se, en) in enumerate(se_en.items()):

        if en < 0:

            di = "<"

        else:

            di = ">"

        pv_[ie] = get_p_value(en, array([se_ra[se] for se_ra in se_ra_]), di)

    return pv_, get_q_value(pv_)
