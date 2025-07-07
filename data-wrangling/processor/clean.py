import pandas as pd
import polars as pl
import time

from load_data import read_pandas
from load_data import read_polars

pandas_data = read_pandas("online_retail_II.xlsx")
polar_data = read_polars("online_retail_II.xlsx")


def pandas_data_cleaning(data):
    """This function cleans the pandas dataset
    """
    # Data cleaning in pandas

    copy_pandas = data.copy()

    # convert all column names to lowercase and replace space with underscore
    copy_pandas.columns = copy_pandas.columns.str.lower().str.replace(" ", "_")
    # checking for missing values
    copy_pandas.isnull().sum()
    # There are null values in the Description and Customer ID columns, I will fill the both columns with zeros.

    # filling null values with zeros
    copy_pandas["description"] = copy_pandas["description"].fillna("0")
    copy_pandas["customer_id"] = copy_pandas["description"].fillna("0")

    copy_pandas.isnull().sum()

    # checking for duplicated rows
    copy_pandas[copy_pandas.duplicated()]
    # There are 34335 rows that are duplicated in the table

    # Keep the first occurence of the duplicates
    copy_pandas = copy_pandas.drop_duplicates(keep="first")
    return copy_pandas


def polars_data_cleaning(data):
    """This function cleans the polars dataset
    """
    # Data cleaning in polars
    #pl_df = read_polars(data)

    # Turning the column names to lowercase and replacing spaces with underscore
    col = []
    for i in data.columns:
        if " " in i:
            out = i.replace(" ", "_").lower()
            col.append(out)
        else:
            col.append(i.lower())
    data.columns = col

    # checking for missing values
    data.null_count()

    # Polars identify more null values in the invoice column
    data.filter(pl.col("invoice").is_null())

    # filling bull values with zeros
    data = data.fill_null(0)

    # checking for duplicates
    data.filter(data.is_duplicated())

    # dropping duplicates
    data = data.unique(keep="first")

    return data    


pd_clean = pandas_data_cleaning(pandas_data)
# print(pd_clean)
