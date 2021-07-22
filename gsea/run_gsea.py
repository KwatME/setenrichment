from ._normalize_each_sample import _normalize_each_sample
from .run_prerank_gsea import run_prerank_gsea


def run_gsea(
    sc_ge_sa,
    sa_la,
    gm,
    no="-0-",
    ra="si",
    **ke,
):
    """
    sc_ge_sa (DataFrame): Gene-by-sample scores
    sa_la (Series): Sample labels
    gm (DataFrame|dict): .GMT | set-to-genes

    no (str): Normalization method: "-0-", "0-1", "sum", "rank average", "rank min", "rank max", "rank dense", "rank ordinal", "log"
    ra (str): Ranking method: "signal to noise", "information coefficient", "difference", "ratio", "log ratio"

    Keyword arguments of run_prerank_gsea...
    """

    sc_ge_sa = _normalize_each_sample(sc_ge_sa, no)

    sa_la, ra

    ge_sc = sc_ge_sa.sum(axis=1)

    return run_prerank_gsea(ge_sc, gm, **ke)
