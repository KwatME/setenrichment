def score_n_sample_n_set(element_x_sample, set_to_element_, n_job=1):

    send(None, element_x_sample, None, set_to_element_)

    Main.n_job = n_job

    set_x_sample = Main.eval(
        """
    Pandas.DataFrame(score_set(
        element_x_sample,
        set_to_element_;
        n_job = n_job,
    ))
    """
    )

    return set_x_sample.set_index("Set")
