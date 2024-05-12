import pytest
import os
import requests
from dotenv import load_dotenv

load_dotenv()

@pytest.mark.asyncio
async def test_get_items():
    db_url = os.getenv("DATABASE_URL")
    if db_url is None:
        pytest.skip("Database URL not found in environment variables")

    url = "http://localhost:8000/users/1"

    response = requests.get(url)

    assert response.status_code == 200

    assert "items" in response.json()
