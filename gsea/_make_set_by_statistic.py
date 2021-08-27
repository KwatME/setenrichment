from pandas import DataFrame


def _make_set_by_statistic(se_en, pv_, qv_):

    return DataFrame(
        data={"Enrichment": se_en.values(), "P-Value": pv_, "Q-Value": qv_}, index=se_en
    ).sort_values("Enrichment", ascending=False)
