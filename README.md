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
sc_el_sa (DataFrame): Scores as element-by-sample
se_el_ (dict of str to list of str): Sets as set-to-element

mi (int): Minimum set size
ma (int): Maximum set size
we (float): Weight used for enrichment method "ks" and "auc"
al (str): Algorithm for enrichment: "ks", "auc", or "js"

pa (str): Directory path to write enrichment_set_sample.tsv
```

### run_prerank_gsea

```
el_sc (Series): Scores sorted
se_el_ (dict of str to list of str): Sets as set-to-element

mi (int): Minimum set size
ma (int): Maximum set size
we (float): Weight used for enrichment method "ks" and "auc"
al (str): Algorithm for enrichment: "ks", "auc", or "js"
ra (int): Random seed
n_pe (int): Number of permutations
n_pl (int): Number of extreme sets to plot
ad (list of str): Additional sets to plot

pa (str): Directory path to write statistic.tsv and plots
```

### run_gsea

```
la_ (list): Sample labels
sc_el_sa (DataFrame): Scores as element-by-sample
se_el_ (dict of str to list of str): Sets as set-to-element

fu (str): Function for rank: "signal to noise", "median difference", or "median ratio"
pe (str): Permutation type: "label" or "set"

mi (int): Minimum set size
ma (int): Maximum set size
we (float): Weight used for enrichment method "ks" and "auc"
al (str): Algorithm for enrichment: "ks", "auc", or "js"
ra (int): Random seed
n_pe (int): Number of permutations
n_pl (int): Number of extreme sets to plot
ad (list of str): Additional sets to plot

pa (str): Directory path to write statistic.tsv and plots
```

## Discuss

To report a bug, request a feature, or leave a comment (about anything related to this project), just [submit an issue](https://github.com/KwatME/gsea/issues/new/choose).
