import pytest
from scraper import generate_content

def test_scraper():
     """This test checks the ouput of the scraper function
     """
     result = generate_content(["Ibadan", "Lagos", "Jos"]) 
     assert result == tuple(result)