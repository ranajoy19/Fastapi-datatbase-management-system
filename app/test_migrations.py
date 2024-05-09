# test_user_model.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User
from database import DATABASE_URL
def test_user_model_has_created_at():
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the User model to check for the 'created_at' attribute
    user = session.query(User).first()

    # Check if the 'created_at' attribute exists in the model
    assert hasattr(user, 'created_at'), "User model does not have 'created_at' attribute"

    session.close()


