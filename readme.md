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


# create a file named test_views.py to test some api responses cases
# 1) you can RUN it using terminal by typing "pytest" navigate to right path 


# Task-2


# a) Add new columns to one of the tables:

# alembic revision --autogenerate -m "add_new_columns"


# b) Delete a column from one of the tables:

# alembic revision --autogenerate -m "delete_column"

# like that we will write upto g

# than create a auto migrations script to run those migrations manuallly





## Setup Instructions

### Step 1: Clone the Repository

```bash
git clone https://github.com/ranajoy19/Fastapi-datatbase-management-system.git
cd Fastapi-datatbase-management-system

### Step 2: create .env file

Create a .env file in the root of the project with the following content:
DATABASE_URL = youtdbUrl
POSTGRES_DB=yourdbname
POSTGRES_USER=yourdbuser
POSTGRES_PASSWORD=yourdbpassword


Step 3: Build and Run the Containers

Use Docker Compose to build and start the containers:

docker-compose up --build


This command will:

Build the Docker images.
Start the FastAPI application.
Start a PostgreSQL database container.


Step 4: Access the Application
Once the containers are up and running, you can access the FastAPI application at:

http://localhost:8000



Database Migrations
To apply database migrations:

docker-compose exec app alembic upgrade head

