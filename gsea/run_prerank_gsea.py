from kwat.significance import get_p_value, get_q_value
from numpy import array, nan
from numpy.random import choice, seed
from pandas import DataFrame

from ._select_gene_sets import _select_gene_sets
from .score_1_n import score_1_n


def run_prerank_gsea(
    ge_sc,
    se_ge_,
    mi=5,
    ma=500,
    we=1.0,
    me="ks",
    se=1729,
    n_pe=100,
    n_pl=25,
    ad=None,
    pa="",
):
    """
    ge_sc (Series): Gene scores
    se_ge_ (dict of str to list of str): set-to-genes

    mi (int): Minimum gene set size
    ma (int): Maximum gene set size
    we (float): Weight used for enrichment method "ks" and "auc"
    me (str): Enrichment method: "ks", "auc", or "js"
    se (int): Random seed
    n_pe (int): Number of permutations
    n_pl (int): Number of extreme gene sets to plot
    ad (list of str): Additional gene sets to plot

    pa (str): Directory path to write the statistic.tsv and plots
    """

    se_ge_ = _select_gene_sets(se_ge_, mi, ma)

    se_en = score_1_n(ge_sc, se_ge_, we=we, me=me)

    se_pv = {}

    if 0 < n_pe:

        print("Computing p-values by permuting sets...")

        seed(se)

        se_si = {se: len(ge_) for se, ge_ in se_ge_.items()}

        ge_ = ge_sc.index.values

        se_enr_ = []

        for ie in range(n_pe):

            print("\t{}/{}".format(ie + 1, n_pe))

            se_enr_.append(
                score_1_n(
                    ge_sc,
                    {
                        se: choice(ge_, size=si, replace=False)
                        for se, si in se_si.items()
                    },
                    we=we,
                    me=me,
                )
            )

        for se, en in se_en.items():

            if en < 0:

                di = "<"

            else:

                di = ">"

            se_pv[se] = get_p_value(en, array([se_enr[se] for se_enr in se_enr_]), di)

    else:

        se_pv = nan

    nu_se_st = DataFrame({"Enrichment": se_en, "P-Value": se_pv})

    nu_se_st["Q-Value"] = get_q_value(nu_se_st["P-Value"].values)

    n_pl, ad

    if pa != "":

        nu_se_st.to_csv("{}/statistics.tsv".format(pa), sep="\t")

    return nu_se_st
