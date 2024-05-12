#docker-compose up --build
# Run docker-compose.yaml with the database version  it should migrate the database version to 9259a6edad0a (c)

# to simulate migrating from version '8948c2cca505' to 'b701adb4ee94'

# alembic downgrade 8948c2cca505

# than >= docker-compose up --build

# This should migrate the database to version 'b701adb4ee94'.

# to run the pytest

# docker-compose run app pytest test_database.py

 