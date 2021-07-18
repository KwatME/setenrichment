def score_1_sample_1_set(element_score_, set_element_, sort=True, plot=True):

    send(element_score_, None, set_element_, None)

    Main.sort = sort

    Main.plot = plot

    result = Main.eval(
        """
    score_set(
        element_,
        score_,
        set_element_;
        sort = sort,
        plot = plot,
    )
    """
    )

    return result
