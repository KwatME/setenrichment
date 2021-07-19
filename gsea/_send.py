from . import Main


def _send(el_sc, el1_, se_el1_, sc_el_sa):

    if el_sc is not None:

        Main.el_ = list(el_sc.index)

        Main.sc_ = list(el_sc)

    if el1_ is not None:

        Main.el1_ = list(el1_)

    if se_el1_ is not None:

        Main.se_el1_ = se_el1_

        Main.eval(
            """
            se_el1_ = convert(Dict{String, Vector{String}}, se_el1_)
        """
        )

    if sc_el_sa is not None:

        Main.sc_el_sa = sc_el_sa

        Main.eval(
            """
            sc_el_sa = DataFrames.DataFrame(Pandas.DataFrame(sc_el_sa))
        """
        )
