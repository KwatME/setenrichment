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
    n_pe=1000,
    n_pl=25,
    ad=None,
    pa="",
):
    """
    ge_sc (Series): Gene scores
    se_ge_ (dict): set-to-genes

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

    se, n_pe

    pv_ = None

    qv_ = None

    nu_se_st = DataFrame({"Enrichment": se_en, "P-Value": pv_, "Q-Value": qv_})

    n_pl, ad

    if pa != "":

        nu_se_st.to_csv("{}/statistics.tsv".format(pa), sep="\t")

    return nu_se_st
