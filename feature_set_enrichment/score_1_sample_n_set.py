def score_1_sample_n_set(element_score_, set_to_elements, sort=True):

    send(element_score_, None, None, set_to_element_)

    Main.sort = sort

    set_to_retsult = Main.eval(
        """
    score_set(
        element_,
        score_,
        set_to_element_;
        sort = sort,
    )
    """
    )

    return set_to_retsult
