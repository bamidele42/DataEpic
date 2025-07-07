import pandas as pd
import polars as pl
import time


from load_data import read_pandas
from load_data import read_polars
from clean import pandas_data_cleaning
from clean import polars_data_cleaning


pandas_data = read_pandas("online_retail_II.xlsx")
polar_data = read_polars("online_retail_II.xlsx")

pd_clean = pandas_data_cleaning(pandas_data)
pl_clean = polars_data_cleaning(polar_data)


def pandas_agg(clean_data):
    """Grouping by country and getting the mean price, sum and count of"""
    pandas_grouped = copy_pandas.groupby("country")[["price", "quantity"]].agg(
        {"price": "mean", "quantity": "count"})
    return pandas_grouped


def polars_agg(clean_data):
    """Group the data by country, average quantity and price"""
    polars_grouped = clean_data.group_by("country").agg(
        [pl.mean("quantity"), pl.mean("price")]).sort(by="price", descending=True)
    return polars_grouped
