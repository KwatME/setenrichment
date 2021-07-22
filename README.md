## Install

### Python modules

```sh
# This module
python -m pip install git+https://github.com/KwatME/gsea

# Helper
python -m pip install git+https://github.com/KwatME/kwat.py
```

### Julia

[Version 1.5.4](https://julialang.org/downloads/oldreleases)

Check if julia 1.5.4 runs in the commond line

```sh
julia --version
```

May need to link (and make it visible by the command line)

```sh
ln -s /Applications/Julia-1.5.app/Contents/Resources/julia/bin/julia /usr/local/bin
```

### Julia modules

```sh
julia --eval '
using Pkg: add

add(url="https://github.com/KwatME/Kwat.jl") # Core algorithm and helper

for na in [
    "PyCall", # Interface between python and julia
    "DataFrames",
    "Pandas",
]

    add(na)

end
'
```

## Test

### Julia core algorithm

```sh
julia --eval '
using Kwat.feature_set_enrichment: score_set

el_ = ["A", "B"]

sc_ = [-1., 1.]

el1_ = ["B"]

println(score_set(el_, sc_, el1_; pl = false))

println("Good.")
'
```

### Python interface

```sh
python -c '
from pandas import Series

el_sc = Series([-1., 1.], index=["A", "B"])

el1_ = ["B"]

from gsea import score_1_1

print(score_1_1(el_sc, el1_, pl=False))

print("Great!")
'
```

## Use

See [examples](nb).

## Documentation

### run_single_sample_gsea

```
gsea.run_single_sample_gsea = run_single_sample_gsea(sc_ge_sa, se_ge_, no='-0-', mi=5, ma=500, we=1.0, me='ks', pa='')
    sc_ge_sa (DataFrame): Gene-by-sample score
    se_ge_ (dict of str to list of str): set-to-genes

    no (str): Normalization method: "-0-", "0-1", "sum", "rank average", "rank min", "rank max", "rank dense", "rank ordinal", or "log"
    mi (int): Minimum gene set size
    ma (int): Maximum gene set size
    we (float): Weight used for enrichment method "ks" and "auc"
    me (str): Enrichment method: "ks", "auc", or "js"

    pa (str): .TSV file path to write the gene-set-by-sample output
```

### run_prerank_gsea

```
gsea.run_prerank_gsea = run_prerank_gsea(ge_sc, se_ge_, mi=5, ma=500, we=1.0, me='ks', se=1729, n_pe=1000, n_pl=25, ad=None, pa='')
    ge_sc (Series): Gene scores
    se_ge_ (dict): set-to-genes

    mi (int): Minimum gene set size
    ma (int): Maximum gene set size
    we (float): Weight used for enrichment method "ks" and "auc"
    me (str): Enrichment method: "ks", "auc", or "js"
    se (int): Random seed
    n_pe (int): Number of permutations
    n_pl (int): Number of extreme gene sets to plot
    ad (list of str): Additional gene sets to plot

    pa (str): Directory path to write the statistic.tsv and plots
```

### run_gsea

```
gsea.run_gsea = run_gsea(sc_ge_sa, sa_la, se_ge_, no='-0-', ra='si', pe='label', **ke)
    sc_ge_sa (DataFrame): Gene-by-sample scores
    sa_la (Series): Sample labels
    se_ge_ (dict of str to list of str): set-to-genes

    no (str): Normalization method: "-0-", "0-1", "sum", "rank average", "rank min", "rank max", "rank dense", "rank ordinal", or "log"
    ra (str): Ranking method: "signal to noise", "information coefficient", "difference", "ratio", or "log ratio"
    pe (str): Permutation type: "label" or "set"

    Keyword arguments of run_prerank_gsea...
```

## Discuss

To report a bug, request a feature, or leave a comment (about anything related to this project), just [submit an issue](https://github.com/KwatME/gsea/issues/new/choose).
