from julia import Main

Main.eval(
    """
    using Kwat.FeatureSetEnrichment: score_set
    using DataFrames
    using Pandas
"""
)

from .score_1_sample_1_set import score_1_sample_1_set
from .score_1_sample_n_set import score_1_sample_n_set
from .score_n_sample_n_set import score_n_sample_n_set
