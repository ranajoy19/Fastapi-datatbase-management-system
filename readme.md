# install this basic installed for task 1 
pip install fastapi 
pip install sqlalchemy 
pip install psycopg2
pip install alembic


# data migration and migrate commamnd 

# 1) set the  sqlalchemy.url inside alembic.ini
# 2) run alembic revision --autogenerate -m "initial migration" to  create initial migration:
# 3) alembic upgrade head to migrate the database


# add dummy data to db using sqlalchemy session
