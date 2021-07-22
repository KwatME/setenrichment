from ._combine_gene_set_enrichments import _combine_gene_set_enrichments
from ._normalize_each_sample import _normalize_each_sample
from ._select_gene_sets import _select_gene_sets
from .score_n_n import score_n_n


def run_single_sample_gsea(
    sc_ge_sa,
    se_ge_,
    no="-0-",
    mi=5,
    ma=500,
    we=1.0,
    me="ks",
    pa="",
):
    """
    sc_ge_sa (DataFrame): Gene-by-sample score
    se_ge_ (dict of str to list of str): set-to-genes

    no (str): Normalization method: "-0-", "0-1", "sum", "rank average", "rank min", "rank max", "rank dense", "rank ordinal", or "log"
    mi (int): Minimum gene set size
    ma (int): Maximum gene set size
    we (float): Weight used for enrichment method "ks" and "auc"
    me (str): Enrichment method: "ks", "auc", or "js"

    pa (str): .TSV file path to write the gene-set-by-sample output
    """

    sc_ge_sa = _normalize_each_sample(sc_ge_sa, no)

    se_ge_ = _select_gene_sets(se_ge_, mi, ma)

    en_se_sa = score_n_n(sc_ge_sa, se_ge_, me=me, we=we)

    en_se_sa = _combine_gene_set_enrichments(en_se_sa)

    if pa != "":

        en_se_sa.to_csv(pa, sep="\t")

    return en_se_sa
