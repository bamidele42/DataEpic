from fastapi import FastAPI
import uvicorn
from scraper import generate_content

app = FastAPI()


@app.get("/")
async def root():
    return generate_content(["Ibadan", "Lagos", "Jos"])


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
