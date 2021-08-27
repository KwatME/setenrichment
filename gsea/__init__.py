from julia import Main

Main.eval(
    """
    using Kwat.feature_set_enrichment: score_set, score_set_new
    using DataFrames
    using Pandas
"""
)

from ._compare_with_target import _compare_with_target
from ._get_p_q import _get_p_q
from ._make_set_by_statistic import _make_set_by_statistic
from ._score_1_1 import _score_1_1
from ._score_1_n import _score_1_n
from ._score_n_n import _score_n_n
from ._select_set import _select_set
from ._send_to_julia import _send_to_julia
from .run_gsea import run_gsea
from .run_prerank_gsea import run_prerank_gsea
from .run_single_sample_gsea import run_single_sample_gsea
