# Assignment

## How to Build and Run the Project in Docker

### Step 1: Create and Update `.env` from `env.example`

First, create a copy of the `env.example` file and name it `.env`. Make sure to update the `.env` file with the required configuration settings.

### Step 2: Build and Run the Project

To build and run the project in Docker, use the following command:

```shell
docker-compose up -d --build
```

If you've already built the project and just want to run it, use:

```shell
docker-compose up -d
```

These steps will create a PostgreSQL container, set up the database, and apply any necessary migrations.

### Step 3: Create a Django-Admin Super User
To create a Django-Admin superuser for your project, run the following command:

```shell
docker exec -it autocompany python manage.py createsuperuser
```

Follow the prompts to set up the superuser account.

### Step 4: Access the API Swagger Documentation
You can access the API Swagger documentation by navigating to the following URL in your web browser:

[http://127.0.0.1/api/schema/docs/](http://127.0.0.1/api/schema/docs/)

This will provide detailed documentation for your API endpoints.
