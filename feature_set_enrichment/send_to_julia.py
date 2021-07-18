def send_to_julia(element_score_, element_x_sample, set_element, set_to_element_):

    if element_score_ is not None:

        Main.element_ = list(element_score_.index)

        Main.score_ = list(element_score_)

    if element_x_sample is not None:

        Main.element_x_sample = element_x_sample

        Main.eval(
            """
        element_x_sample = DataFrames.DataFrame(Pandas.DataFrame(element_x_sample))
        """
        )

    if set_element_ is not None:

        Main.set_element_ = list(set_element_)

    if set_to_element_ is not None:

        Main.set_to_element_ = set_to_element_

        Main.eval(
            """
        set_to_element_ = convert(Dict{String, Vector{String}}, set_to_element_)
        """
        )
