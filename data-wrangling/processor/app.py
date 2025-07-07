from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from fastapi.exceptions import HTTPException
import csv
import io
import uvicorn
import polars as pl
import pandas as pd
import os
import json

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = os.path.join(BASE_DIR, "uploads")


@app.get("/")
def read_root():
    msg = "This Api uploads data and processed it"
    return f"{msg}"


@app.post("/process-data")
async def upload_file(file: UploadFile = File(...)):
    if not file.filename.endswith((".xlsx", ".xls")):
        raise HTTPException(
            status_code=400, detail="Invalid file format. Please upload an Excel file.")
    else:
        content = await file.read()
        df = pl.read_excel(io.BytesIO(content))

        # Turning the column names to lowercase and replacing spaces with underscore
        col = []
        for i in df.columns:
            if " " in i:
                out = i.replace(" ", "_").lower()
                col.append(out)
            else:
                col.append(i.lower())
        df.columns = col

    # checking for missing values
        df.null_count()

    # Polars identify more null values in the invoice column
        df.filter(pl.col("invoice").is_null())

    # filling bull values with zeros
        df = df.fill_null(0)

    # checking for duplicates
        df.filter(df.is_duplicated())

    # dropping duplicates
        df = df.unique(keep="first")

    # Group the data by country, average quantity and price
        polars_grouped = df.group_by("country").agg(
            [pl.mean("quantity"), pl.mean("price")]).sort(by="price", descending=True)
        heads = polars_grouped.head(5)

    return heads.to_dicts()


@app.post("/file/download-json")
async def download(file: UploadFile):
    if not file.filename.endswith((".xlsx", ".xls")):
        raise HTTPException(
            status_code=400, detail="Invalid file format. Please upload an Excel file")
    else:
        content = await file.read()
        df = pd.read_excel(io.BytesIO(content))

        # convert all column names to lowercase and replace space with underscore
        df.columns = df.columns.str.lower().str.replace(" ", "_")

        # checking for missing values
        df.isnull().sum()

        # There are null values in the Description and Customer ID columns, I will fill the both columns with zeros.

        # filling null values with zeros
        df["description"] = df["description"].fillna("0")
        df["customer_id"] = df["description"].fillna("0")

        # checking for duplicated rows
        df[df.duplicated()]
        # There are 34335 rows that are duplicated in the table

        df = df.drop_duplicates(keep="first")

        # first ten rows
        first_ten = df.head(10).to_json()

        new_filename = f"{os.path.splitext(file.filename)[0]}.json"

        # write the data to a file
        SAVE_FILE_PATH = os.path.join(UPLOAD_DIR, new_filename)
        with open(SAVE_FILE_PATH, "w") as f:
            json.dump(first_ten, f)

    return FileResponse(path=SAVE_FILE_PATH, media_type="application/octet-stream", filename=new_filename)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
