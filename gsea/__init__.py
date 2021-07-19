from julia import Main

Main.eval(
    """
    using Kwat.FeatureSetEnrichment: score_set, score_set_new
    using DataFrames
    using Pandas
"""
)

from ._score_1_1 import _score_1_1
from ._score_1_n import _score_1_n
from ._score_n_n import _score_n_n
from .run_gsea import run_gsea
from .run_prerank_gsea import run_prerank_gsea
from .run_single_sample_gsea import run_single_sample_gsea
