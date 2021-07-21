from pandas import DataFrame

from ._convert_gmt_to_dict import _convert_gmt_to_dict
from ._select_gene_sets import _select_gene_sets
from .score_1_n import score_1_n


def run_prerank_gsea(
    ge_sc,
    gm,
    mi=5,
    ma=500,
    we=1.0,
    me="ks",
    se=1729,
    pe="label",
    n_pe=1000,
    n_pl=25,
    ad=None,
    pa="",
):

    gm = _convert_gmt_to_dict(gm)

    se_ge_ = _select_gene_sets(gm, mi, ma)

    se_en = score_1_n(ge_sc, se_ge_, we=we, me=me)

    se, pe, n_pe

    pv_ = None

    qv_ = None

    nu_se_st = DataFrame({"Enrichment": se_en, "P-Value": pv_, "Q-Value": qv_})

    n_pl, ad

    if pa != "":

        nu_se_st.to_csv("{}/statistics.tsv".format(pa), sep="\t")

    return nu_se_st
