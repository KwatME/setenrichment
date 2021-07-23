from . import Main


def _send_to_julia(el_sc, sc_el_sa, el_, se_el_, we, al):

    if el_sc is not None:

        Main.el_ = list(el_sc.index)

        Main.sc_ = list(el_sc)

    if sc_el_sa is not None:

        Main.sc_el_sa = sc_el_sa

        Main.eval(
            """
            sc_el_sa = DataFrames.DataFrame(Pandas.DataFrame(sc_el_sa))
        """
        )

    if el_ is not None:

        Main.el1_ = list(el_)

    if se_el_ is not None:

        Main.se_el_ = se_el_

        Main.eval(
            """
            se_el_ = convert(Dict{String, Vector{String}}, se_el_)
        """
        )

    if we is not None:

        Main.we = we

        Main.eval(
            """
            we = convert(Float64, we)
        """
        )

    if al is not None:

        Main.al = al
