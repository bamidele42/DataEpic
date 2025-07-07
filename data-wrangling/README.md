# Data Processing API

## Overview

This project implements a FastAPI-based web service designed for processing large datasets using both Pandas and Polars. It provides efficient data loading, cleaning, and aggregation functionalities, demonstrating the superior performance of Polars in reading and aggregation tasks compared to Pandas.

The API exposes endpoints for:

- Processing and aggregating data
- Downloading processed output files

## Installation and Setup

This project uses **Poetry** for dependency management. All required dependencies are listed in the `pyproject.toml` file.

To install dependencies, run:

```sh
poetry install
```

## Project Structure

### Scripts

1. **`load_data.py`**: Loads data using Pandas and Polars, returning a DataFrame along with the time taken by each library.
2. **`clean.py`**: Imports data from `load_data.py`, cleans it, and returns a cleaned DataFrame using both Pandas and Polars.
3. **`aggregate.py`**: Imports cleaned data from `clean.py`, performs aggregation operations, and returns an aggregated DataFrame.

## API Endpoints

The API is implemented in FastAPI and can be run using Uvicorn.

To start the server:

```sh
uvicorn main:app --reload
```

### Aggregation Endpoints

- `GET /pandas-agg` – Returns aggregated data using the Pandas library.
- `GET /polar-agg` – Returns aggregated data using the Polars library.

### Data Processing Endpoints

To start the app for processing and downloading data:

```sh
uvicorn app:app --reload
```

- `POST /process-data` – Accepts `.xls` or `.xlsx` files, processes them, and returns an aggregated output.
- `POST /file/download-json` – Accepts `.xls` or `.xlsx` files and provides a downloadable JSON file of processed data.

## Conclusion

This project demonstrates efficient data processing techniques using Pandas and Polars within a FastAPI web service, optimizing performance for large datasets.
