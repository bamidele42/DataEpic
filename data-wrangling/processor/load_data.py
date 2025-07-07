import pandas as pd
import polars as pl
import time


def read_pandas(data):
    """This function loads data using pandas and returns loaded data and time taken 
    """
    pandas_start = time.time()
    pd_sheet1 = pd.read_excel(data, sheet_name="Year 2009-2010")
    pd_sheet2 = pd.read_excel(data, sheet_name="Year 2010-2011")

    pd_df = pd.concat([pd_sheet1, pd_sheet2], axis=0, ignore_index=True)
    pandas_end = time.time()
    pandas_load_time = pandas_end - pandas_start
    print(f"Pandas load time: {pandas_load_time}")

    return pd_df


def read_polars(data):
    """This function loads data using polars and returns loaded data and time taken 
    """
    polars_start = time.time()
    pl_sheet1 = pl.read_excel(data, sheet_name="Year 2009-2010")
    pl_sheet2 = pl.read_excel(data, sheet_name="Year 2010-2011")

    pl_df = pl.concat([pl_sheet1, pl_sheet2], how="vertical")
    polars_end = time.time()
    polars_load_time = polars_end - polars_start
    print(f"Polars load time: {polars_load_time}")
    return pl_df


pandas_data = read_pandas("online_retail_II.xlsx")

polar_data = read_polars("online_retail_II.xlsx")

# print(pandas_data)
