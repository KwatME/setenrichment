from kwat.significance import get_p_value, get_q_value
from numpy import array
from numpy.random import seed, shuffle
from pandas import DataFrame

from .compare_with_target import compare_with_target
from .run_prerank_gsea import run_prerank_gsea
from .score_1_n import score_1_n
from .select_set import select_set


def run_gsea(
    #
    ta,
    sc_el_sa,
    se_el_,
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
    sc_el_sa (DataFrame): Gene by sample
    se_el_ (dict of str to list of str): Gene set to genes

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

    el_sc = compare_with_target(ta, sc_el_sa, fu, n_jo=n_jo)

    se_el_ = select_set(se_el_, mi, ma)

    # TODO: sort the columns once and then compare_with_target
    if pe == "label":

        se_en = score_1_n(el_sc, se_el_, we=we, al=al)

        print("Permuting labels to compute p-values...")

        se_ra_ = []

        sh = ta.copy()

        seed(ra)

        for ie in range(n_pe):

            print("  {}/{}".format(ie + 1, n_pe))

            shuffle(sh)

            se_ra_.append(
                score_1_n(
                    compare_with_target(sh, sc_el_sa, fu, n_jo=n_jo),
                    se_el_,
                    we=we,
                    al=al,
                )
            )

        se_pv = {}

        for se, en in se_en.items():

            if en < 0:

                di = "<"

            else:

                di = ">"

            se_pv[se] = get_p_value(en, array([se_ra[se] for se_ra in se_ra_]), di)

        nu_se_st = DataFrame({"Enrichment": se_en, "P-Value": se_pv})

        nu_se_st["Q-Value"] = get_q_value(nu_se_st["P-Value"].values)

        nu_se_st.sort_values("Enrichment", ascending=False, inplace=True)

        n_pl

        ad

        if pa != "":

            nu_se_st.to_csv("{}/statistics.tsv".format(pa), sep="\t")

        return nu_se_st

    elif pe == "set":

        return run_prerank_gsea(
            el_sc,
            se_el_,
            mi=mi,
            ma=ma,
            we=we,
            al=al,
            ra=ra,
            n_pe=n_pe,
            n_pl=n_pl,
            ad=ad,
            pa=pa,
        )
