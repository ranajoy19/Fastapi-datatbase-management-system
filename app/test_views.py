from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models import User, Post
from views import router,get_db
from main import app
from fastapi.testclient import TestClient
from schema import UserSchema, PostSchema


client = TestClient(app)


def test_user_exists():

    # givving random user_id that is existed in the database
    user_id = [1,2,4]

    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    user_data = response.json()
    assert UserSchema(**user_data)  
    assert user_data["id"] in user_id  


def test_user_not_found():
    response = client.get("/users/999")  # there is no user having 999 as a id 
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"