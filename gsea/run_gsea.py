from numpy.random import seed, shuffle

from ._compare_with_target import _compare_with_target
from ._get_p_q import _get_p_q
from ._make_set_by_statistic import _make_set_by_statistic
from ._score_1_n import _score_1_n
from ._select_set import _select_set
from .run_prerank_gsea import run_prerank_gsea


def run_gsea(
    #
    ta,
    sc_fe_sa,
    se_fe_,
    #
    fu="signal_to_noise",
    #
    mi=5,
    ma=500,
    #
    n_jo=1,
    we=1.0,
    al="ks",
    #
    pe="label",
    #
    ra=1729,
    #
    n_pe=100,
    n_pl=25,
    ad=None,
    #
    pa="",
):
    """
    ta (array): Target sample labels
    sc_fe_sa (DataFrame): Gene by sample
    se_fe_ (dict of str to list of str): Gene set to genes

    fu (str): Ranking function: "signal_to_noise", "mean_difference", "mean_ratio", "median_difference", "median_ratio", "cosine_distance", or "pearson_correlation"

    mi (int): Minimum set size
    ma (int): Maximum set size

    n_jo (int): Number of threads
    we (float): Weight for enrichment algorithm "ks" and "auc"
    al (str): Enrichment algorithm: "ks", "auc", or "js"

    pe (str): Permutation type: "label" or "set"

    ra (int): Random seed

    n_pe (int): Number of permutations
    n_pl (int): Number of extreme sets to plot
    ad (list of str): Additional sets to plot

    pa (str): Directory path to write statistic.tsv and plots
    """

    fe_sc = _compare_with_target(ta, sc_fe_sa, fu, n_jo=n_jo)

    se_fe_ = _select_set(se_fe_, mi, ma)

    if pe == "label":

        se_en = _score_1_n(fe_sc, se_fe_, we=we, al=al)

        if 0 < n_pe:

            print("Permuting labels to compute p-values...")

            tac = ta.copy()

            se_ra_ = []

            seed(seed=ra)

            for ie in range(n_pe):

                print("  {}/{}".format(ie + 1, n_pe))

                shuffle(tac)

                se_ra_.append(
                    _score_1_n(
                        _compare_with_target(tac, sc_fe_sa, fu, n_jo=n_jo),
                        se_fe_,
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

    elif pe == "set":

        return run_prerank_gsea(
            fe_sc,
            se_fe_,
            mi=mi,
            ma=ma,
            n_jo=n_jo,
            we=we,
            al=al,
            ra=ra,
            n_pe=n_pe,
            n_pl=n_pl,
            ad=ad,
            pa=pa,
        )
