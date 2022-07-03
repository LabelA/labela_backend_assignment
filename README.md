# Assignment

Hello Welcome to Alicia test. This is an auto company application which uses the tech stack below.

- Python (Django and Django rest framework) for development
- Relational database - PostgreSQL
- Database ORM, because using a standard is faster and more secure (default provided by Django)

## User's Story

- As a company, I want all my products in a database, so I can offer them via our new platform to customers
- As a client, I want to add a product to my shopping cart, so I can order it at a later stage
- As a client, I want to remove a product from my shopping cart, so I can tailor the order to what I actually need
- As a client, I want to order the current contents in my shopping cart, so I can receive the products I need to repair my car
- As a client, I want to select a delivery date and time, so I will be there to receive the order
- As a client, I want to see an overview of all the products, so I can choose which product I want
- As a client, I want to view the details of a product, so I can see if the product satisfies my needs

## How to Use the App

### Running as Production

- Create a file named .env-prod and add the following variables
  ```
  SQL_ENGINE = "django.db.backends.postgresql"
  SQL_DATABASE = "UPDATE ME"
  SQL_USER = "UPDATE ME"
  SQL_PASSWORD = "UPDATE ME"
  SQL_HOST = "localhost"
  SQL_PORT = 5432
  SECRET_KEY = "7+om-9__!v%1ud!6-wwkf0hs0x7v1myz9jn#e9d8n@v#1^qk3p"
  DEBUG = 0
  DJANGO_ALLOWED_HOSTS = "localhost 127.0.0.1 [::1]"
  ```
- Run the App

  ```
  docker build -t autocompany:latest .
  docker compose up
  ```

* navigate to http://localhost:8000/admin

- Run the Test

  #### test

  - open a new terminal, while the app is still running and run the commands below

  ```
  docker-compose exec autocompany pytest
  ```

  ### test coverage

  ```
  docker-compose exec autocompany pytest -p no:warnings --cov=.
  ```

### Running as Local or Development

- Create a .env file and add the following variables
  ```
  SECRET_KEY = "7+om-9__!v%1ud!6-wwkf0hs0x7v1myz9jn#e9d8n@v#1^qk3p"
  DEBUG = 0
  DJANGO_ALLOWED_HOSTS = "localhost 127.0.0.1 [::1]"
  ```
- Run migrations

  ```
  python3 manage.py migration
  ```

- Run the App

  ```
  gunicorn autocompany.wsgi:application --bind 0.0.0.0:8000
  ```

* navigate to http://localhost:8000/admin

- Run the Test

  #### test

  ```
  pytest
  ```

  ### test coverage

  ```
  pytest -p no:warnings --cov=.
  ```

## Using admin with Docker

- create admin
  ```
  docker-compose exec autocompany manage.py createsuperuser
  ```
- navigate to http://localhost:8000/admin

## Using admin with Locally or Development

- create admin

  ```
  python manage.py createsuperuser
  ```

- navigate to http://localhost:8000/admin
