import os
import pandas as pd
import polars as pl

from fastapi import FastAPI
import uvicorn

base_dir = os.path.dirname(os.path.abspath(__file__))
pandas_dataset = os.path.join(base_dir, "pandas_agg.json")
polars_dataset = os.path.join(base_dir, "polars_agg.json")


app = FastAPI()


@app.get("/")
def read_root():
    msg = "This Api returns the aggregate data from both Pandas and Polars. use /pandas-agg to view pandas data aggregate use /polars-agg to view polars data aggregate"
    return f"{msg}"


@app.get("/pandas-agg")
def pandas_agg():
    df = pd.read_json(pandas_dataset)
    return df.to_dict()


@app.get("/polars-agg")
def polars_agg():
    df = pl.read_json(polars_dataset)
    return df.to_dicts()


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
