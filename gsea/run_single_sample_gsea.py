from ._score_n_n import _score_n_n
from ._select_set import _select_set


def run_single_sample_gsea(
    #
    sc_fe_sa,
    se_fe_,
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
    sc_fe_sa (DataFrame): Gene by sample
    se_fe_ (dict of str to list of str): Gene set to genes

    mi (int): Minimum set size
    ma (int): Maximum set size

    n_jo (int): Number of threads
    we (float): Weight for enrichment algorithm "ks" and "auc"
    al (str): Enrichment algorithm: "ks", "auc", or "js"

    pa (str): Directory path to write enrichment_set_sample.tsv
    """

    se_fe_ = _select_set(se_fe_, mi, ma)

    en_se_sa = _score_n_n(sc_fe_sa, se_fe_, we=we, al=al)

    if pa != "":

        en_se_sa.to_csv(path_or_buf="{}/enrichment_set_sample.tsv".format(pa), sep="\t")

    return en_se_sa
