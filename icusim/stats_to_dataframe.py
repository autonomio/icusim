def stats_to_dataframe(results):

    import pandas as pd

    # pd.set_option("display.max_rows", 5)
    # pd.set_option("display.max_columns", 7)
    # pd.set_option('display.width', None)

    out = []
    cols = []

    # get day key
    for day in results.keys():

        _temp_ = []
        cols = []

        # get metric name key
        for metric in results[day].keys():

            _temp_.append(results[day][metric]['standard_icu'])
            _temp_.append(results[day][metric]['ventilated_icu'])

            cols.append('standard_icu_' + metric)
            cols.append('ventilated_icu_' + metric)

        out.append(_temp_)

    df = pd.DataFrame(out)
    df.columns = cols

    return df
