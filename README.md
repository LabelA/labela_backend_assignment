# Instructions

Setup
---------


* Clone the repository
* Then in the terminal locate the project directory where the Dockerfile is present
* Type the commands 
    -```docker-compose build```
    -```docker-compose up```
    - Navigate to ```http://127.0.0.1/:8000```
* While running the container open another terminal in the same location and run
    -```docker-compose run app python manage.py makesuperuser``` and create a superuser. You will need this user to add products

API Documentation
---------

* Navigate to the docs folder
* Use command npx serve
* Follow the given address to access the api
