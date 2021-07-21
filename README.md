## Install

Install python modules:

- gsea (this module)
- kwat.py (helper)

```sh
python -m pip install git+https://github.com/KwatME/gsea

python -m pip install git+https://github.com/KwatME/kwat.py
```

Install [julia 1.5.4](https://julialang.org/downloads/oldreleases/)

Check if julia runs in the commond line:

```sh
julia
```

May need to link julia:

```sh
ln -s /Applications/Julia-1.5.app/Contents/Resources/julia/bin/julia /usr/local/bin
```

Install julia modules:

- PyCall (python-julia interface)
- Kwat.jl (core algorithm and helper)

```sh
julia
```

```julia
using Pkg: add

for na in [
    "PyCall",
]

    add(na)

end

add(url="https://github.com/KwatME/Kwat.jl")
```

## Test

Test running the core algorithm:

```sh
julia --eval '
using Kwat.feature_set_enrichment: score_set

el_ = ["A", "B"]

sc_ = [-1., 1.]

el1_ = ["B"]

println(score_set(el_, sc_, el1_; pl = false))

println(":)")
'
```

Test running the python interface:

```sh
python -c '
import pandas as pd

el_sc = pd.Series([-1, 1], index=["A", "B"])

el1_ = ["B"]

import gsea

print(gsea.score_1_1(el_sc, el1_, pl=False))

print(":)")
'
```

## Use

See [examples](nb).

## Documentation

Coming soon...
