from numpy import array, nan
from numpy.random import choice, seed
from pandas import DataFrame

from kwat.significance import get_p_value, get_q_value

from .score_1_n import score_1_n
from .select_set import select_set


def run_prerank_gsea(
    el_sc,
    se_el_,
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
    el_sc (Series): Sorted gene scores
    se_el_ (dict of str to list of str): Gene set to genes

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

    se_el_ = select_set(se_el_, mi, ma)

    se_en = score_1_n(el_sc, se_el_, we=we, al=al)

    se_pv = {}

    if 0 < n_pe:

        print("Permuting sets to compute p-values...")

        seed(seed=ra)

        se_si = {se: len(el_) for se, el_ in se_el_.items()}

        el_ = el_sc.index.values

        se_ra_ = []

        for ie in range(n_pe):

            print("  {}/{}".format(ie + 1, n_pe))

            se_ra_.append(
                score_1_n(
                    el_sc,
                    {
                        se: choice(el_, size=si, replace=False)
                        for se, si in se_si.items()
                    },
                    we=we,
                    al=al,
                )
            )

        for se, en in se_en.items():

            if en < 0:

                di = "<"

            else:

                di = ">"

            se_pv[se] = get_p_value(en, array([se_ra[se] for se_ra in se_ra_]), di)

    else:

        se_pv = nan

    nu_se_st = DataFrame({"Enrichment": se_en, "P-Value": se_pv})

    nu_se_st["Q-Value"] = get_q_value(nu_se_st["P-Value"].values)

    nu_se_st.sort_values("Enrichment", ascending=False, inplace=True)

    n_pl

    ad

    if pa != "":

        nu_se_st.to_csv("{}/statistics.tsv".format(pa), sep="\t")

    return nu_se_st
