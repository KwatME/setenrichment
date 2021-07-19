from ._combine_gene_set_enrichments import _combine_gene_set_enrichments
from ._convert_gmt_to_dict import _convert_gmt_to_dict
from ._normalize_each_sample import _normalize_each_sample
from ._score_n_n import _score_n_n
from ._select_gene_sets import _select_gene_sets


def run_single_sample_gsea(
    sc_ge_sa,
    gm,
    no="-0-",
    mi=5,
    ma=500,
    we=1.0,
    me="ks",
    pa="",
):

    sc_ge_sa = _normalize_each_sample(sc_ge_sa, no)

    gm = _convert_gmt_to_dict(gm)

    se_ge_ = _select_gene_sets(gm, mi, ma)

    en_se_sa = _score_n_n(sc_ge_sa, se_ge_, me=me, we=we)

    en_se_sa = _combine_gene_set_enrichments(en_se_sa)

    if pa != "":

        en_se_sa.to_csv(pa, sep="\t")

    return en_se_sa
