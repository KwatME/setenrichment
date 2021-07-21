## Install

### Python modules

- gsea (this module)
- kwat.py (helper)

```sh
python -m pip install git+https://github.com/KwatME/gsea

python -m pip install git+https://github.com/KwatME/kwat.py
```

### Julia

[Version 1.5.4](https://julialang.org/downloads/oldreleases/)

Check if julia runs in the commond line

```sh
julia
```

May need to link julia (to make it visible by the command line)

```sh
ln -s /Applications/Julia-1.5.app/Contents/Resources/julia/bin/julia /usr/local/bin
```

### Julia modules

- Kwat.jl (core algorithm and helper)
- PyCall (python-julia interface)
- DataFrames
- Pandas

```sh
julia --eval '
using Pkg: add

add(url="https://github.com/KwatME/Kwat.jl")

for na in [
    "PyCall",
    "DataFrames",
    "Pandas",
]

    add(na)

end
'
```

## Test

### Run julia core algorithm

```sh
julia --eval '
using Kwat.feature_set_enrichment: score_set

el_ = ["A", "B"]

sc_ = [-1., 1.]

el1_ = ["B"]

println(score_set(el_, sc_, el1_; pl = false))

println("Good :)")
'
```

### Run python interface

```sh
python -c '
from pandas import Series

el_sc = Series([-1., 1.], index=["A", "B"])

el1_ = ["B"]

from gsea import score_1_1

print(score_1_1(el_sc, el1_, pl=False))

print("Great :D")
'
```

## Use

See [examples](nb).

## Documentation

Coming soon...
