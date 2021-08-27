from . import Main


def _send_to_julia(fe_sc, sc_fe_sa, fe_, se_fe_, we, al):

    if fe_sc is not None:

        Main.fe_ = list(fe_sc.index)

        Main.sc_ = list(fe_sc)

    if sc_fe_sa is not None:

        Main.sc_fe_sa = sc_fe_sa

        Main.eval(
            """
            sc_fe_sa = DataFrames.DataFrame(Pandas.DataFrame(sc_fe_sa))
        """
        )

    if fe_ is not None:

        Main.fe1_ = list(fe_)

    if se_fe_ is not None:

        Main.se_fe_ = se_fe_

        Main.eval(
            """
            se_fe_ = convert(Dict{String, Vector{String}}, se_fe_)
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
