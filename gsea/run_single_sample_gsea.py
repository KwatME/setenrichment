from .score_n_n import score_n_n
from .select_set import select_set


def run_single_sample_gsea(
    #
    sc_el_sa,
    se_el_,
    #
    mi=5,
    ma=500,
    #
    n_jo=1,
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

    n_jo (int): Number of threads
    we (float): Weight for enrichment algorithm "ks" and "auc"
    al (str): Enrichment algorithm: "ks", "auc", or "js"

    pa (str): Directory path to write enrichment_set_sample.tsv
    """

    se_el_ = select_set(se_el_, mi, ma)

    en_se_sa = score_n_n(sc_el_sa, se_el_, we=we, al=al)

    if pa != "":

        en_se_sa.to_csv("{}/enrichment_set_sample.tsv".format(pa), sep="\t")

    return en_se_sa
