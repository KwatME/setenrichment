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

    sc_ge_sa = _normalize_each_sample(sc_ge_sa, no)

    ge_sc = sc_ge_sa.sum(axis=1)  # sa_la, ra

    return run_prerank_gsea(ge_sc, gm, **ke)
