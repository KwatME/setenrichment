## Install

### This GSEA python module

```sh
python -m pip install git+https://github.com/KwatME/gsea
```

### [Julia 1.5.4](https://julialang.org/downloads/oldreleases/)

### Julia modules

```sh
julia
```

```julia
using Pkg: add

for na in [
    "PyCall",
    "DataFrames",
    "Pandas",
]

    add(na)

end

add(url="https://github.com/KwatME/Kwat.jl")
```

## Use

See [examples](nb).

## Documentation

### Prerank GSEA (and GSEA)

as: association metric:
- si: signal to noise
- io: information coefficient
- co: cosine
- di: difference
- ra: ratio
- lo: log ratio
