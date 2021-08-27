from numpy import nan
from numpy.random import choice, seed

from ._get_p_q import _get_p_q
from ._make_set_by_statistic import _make_set_by_statistic
from ._score_1_n import _score_1_n
from ._select_set import _select_set


def run_prerank_gsea(
    fe_sc,
    se_fe_,
    #
    mi=5,
    ma=500,
    #
    n_jo=1,
    we=1.0,
    al="ks",
    #
    ra=1729,
    n_pe=100,
    n_pl=25,
    ad=None,
    #
    pa="",
):
    """
    fe_sc (Series): Sorted gene scores
    se_fe_ (dict of str to list of str): Gene set to genes

    mi (int): Minimum set size
    ma (int): Maximum set size

    n_jo (int): Number of threads
    we (float): Weight for enrichment algorithm "ks" and "auc"
    al (str): Enrichment algorithm: "ks", "auc", or "js"

    ra (int): Random seed
    n_pe (int): Number of permutations
    n_pl (int): Number of extreme sets to plot
    ad (list of str): Additional sets to plot

    pa (str): Directory path to write statistic.tsv and plots
    """

    se_fe_ = _select_set(se_fe_, mi, ma)

    se_en = _score_1_n(fe_sc, se_fe_, we=we, al=al)

    if 0 < n_pe:

        print("Permuting sets to compute p-values...")

        fe_ = fe_sc.index.values

        se_si = {se: len(fe_) for se, fe_ in se_fe_.items()}

        se_ra_ = []

        seed(seed=ra)

        for ie in range(n_pe):

            print("  {}/{}".format(ie + 1, n_pe))

            se_ra_.append(
                _score_1_n(
                    fe_sc,
                    {
                        se: choice(fe_, size=si, replace=False)
                        for se, si in se_si.items()
                    },
                    we=we,
                    al=al,
                )
            )

        pv_, qv_ = _get_p_q(se_en, se_ra_)

    else:

        pv_ = nan

        qv_ = nan

    nu_se_st = _make_set_by_statistic(se_en, pv_, qv_)

    n_pl

    ad

    if pa != "":

        nu_se_st.to_csv(path_or_buf="{}/statistics.tsv".format(pa), sep="\t")

    return nu_se_st
