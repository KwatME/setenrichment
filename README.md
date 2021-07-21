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

May need to link julia.
Link (in macOS):

```sh
ln -s /Applications/Julia-1.5.app/Contents/Resources/julia/bin/julia /usr/local/bin
```

Install julia modules:

- PyCall (links python and julia)
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
julia --eval 'using Kwat.feature_set_enrichment: score_set; println(score_set(["A", "B"], [-1., 1.], ["B"]; pl = false))'
```

Test running the python interface:

```sh
python -c '
import pandas as pd

import gsea

el_sc = pd.Series([-1, 1], index=["A", "B"])

el1_ = ["B"]

print(gsea.score_1_1(el_sc, el1_, pl=False))
'
```

## Use

See [examples](nb).

## Documentation

Coming soon...
