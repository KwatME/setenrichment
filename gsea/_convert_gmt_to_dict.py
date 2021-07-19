def _convert_gmt_to_dict(gm):

    if not isinstance(gm, dict):

        gm = {se: ge_.dropna().tolist() for se, ge_ in gm.iterrows()}

    return gm
