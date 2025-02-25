Here's a professional rewrite of your README file:

---

# **Weather Scraper API**

## **Overview**

This project extracts weather data for three Nigerian states from [Time and Date](https://www.timeanddate.com/weather/nigeria/), processes the data, and writes the cleaned results to a Google Sheet. It also provides a FastAPI-based endpoint for accessing the latest weather data via an interactive API interface.

## **Features**

1. **FastAPI Endpoint** – Provides an API endpoint that scrapes, processes, and stores weather data in real-time. The endpoint is accessible via an interactive Swagger UI (`/docs`).
2. **Dependency Management** – Utilizes Poetry for efficient package management.
3. **Virtual Environment** – Uses `venv` to ensure an isolated Python environment.
4. **Web Scraping** – Implements `requests` and `BeautifulSoup` (`bs4`) to extract relevant weather details from the target webpage.
5. **Data Cleaning** – Cleans extracted data using regular expressions (`re` module in Python).
6. **Google Sheets Integration** – Leverages `gspread` for authentication and seamless updates to a Google Sheet.

## **Installation & Usage**

### **Setup**

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd weather-scraper-api
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows
   ```
3. Install dependencies using Poetry:
   ```bash
   poetry install
   ```
4. Run the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```
5. Access the interactive API documentation at:
   ```
   http://127.0.0.1:8000/docs
   ```

## **Contributing**

Contributions are welcome! Please feel free to submit a pull request or report issues.
