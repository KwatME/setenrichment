from ._select_set import _select_set
from .score_n_n import score_n_n


def run_single_sample_gsea(
    #
    sc_el_sa,
    se_el_,
    #
    mi=5,
    ma=500,
    #
    we=1.0,
    al="ks",
    #
    pa="",
):
    """
    sc_el_sa (DataFrame): Gene by sample
    se_el_ (dict of str to list of str): Gene set to genes

    mi (int): Minimum set size
    ma (int): Maximum set size

    we (float): Weight for enrichment algorithm "ks" and "auc"
    al (str): Enrichment algorithm: "ks", "auc", or "js"

    pa (str): Directory path to write enrichment_set_sample.tsv
    """

    se_el_ = _select_set(se_el_, mi, ma)

    en_se_sa = score_n_n(sc_el_sa, se_el_, we=we, al=al)

    if pa != "":

        en_se_sa.to_csv("{}/enrichment_set_sample.tsv".format(pa), sep="\t")

    return en_se_sa
