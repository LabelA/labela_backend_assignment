# Assignment

Oh, hello!
---------
First of all, awesome that you want to join our team! We already know that you're a cool person, but now we just want to know if you're a cool coder as well! To that end we've set up a basic exercise for you to complete.

**Our tech stack!**

Before we start off, let me elaborate about our tech stack. For most projects, we use the following technologies:

* Python, for rapid development
* Relational database, we mostly use PostgreSQL 
* Widely accepted frameworks, we mostly use the Django Framework
* Database ORM, because using a standard is faster and more secure (default provided by Django)

The assignment
---------
A company specialised in car parts wants to modernise their company, and start selling their parts online. Being the pro car salesmen that they are, they decided to develop the front-end via another agency. They entrust the back-end to none other than Label A.

After some initial research, we've defined the following user stories on top of our backlog:

* As a company, I want all my products in a database, so I can offer them via our new platform to customers
* As a client, I want to add a product to my shopping cart, so I can order it at a later stage
* As a client, I want to remove a product from my shopping cart, so I can tailor the order to what I actually need
* As a client, I want to order the current contents in my shopping cart, so I can receive the products I need to repair my car
* As a client, I want to select a delivery date and time, so I will be there to receive the order
* As a client, I want to see an overview of all the products, so I can choose which product I want
* As a client, I want to view the details of a product, so I can see if the product satisfies my needs

Develop an API according to the user stories defined above. You should not spend more than 8 hours on this exercise, so put on your MVP glasses and prioritise according to what you think the product should minimally entail.

Included in this repository:

* A freshly installed Django Framework (with not admin user -> go to this page to see how to create one: https://docs.djangoproject.com/en/1.8/intro/tutorial02/)
* For convenience you can use .sqllite which is already configured in the project instead of PostgreSQL
* Bonus points if you can include PostgreSQL in a Docker setup -> base Dockerfile is included

We can make the following assumptions:

* We don't have to worry about the front-end, but should think of a data format a JavaScript application can handle
* We don't need to worry about the payment of the order. Who needs money anyway?

How to score bonus points (ergo: we really advise you to tackle it this way):

* Implement a RESTful API
* Use a ORM
* Document how we can set up and instantiate the project, so we can easily test it functionally

If you have any questions, feel free to contact us! Any feedback on this exercise is always welcome!


**Want to run the project in Docker?**

- ```docker build -t autocompany .```
- ``` docker run -p 80:80 -d autocompany```
- Navigate to ```http://127.0.0.1/```

 # Implementation Overview

This project's main scope is to create RESTful endpoints, I created RESTful endpoints. No Frontend designs were done in thi project. But each endpoint will return a readable JSON format. So, the frontend JS applications can read.

So far all endpoints need Admin permission. For further development endpoints will be developed for admin and local user separately. 

Run the Docker file and migrate all the tables to database and createsuperuser user using following commands

```bash
docker-compose up --build
docker exec -it 261e658273912affcde5af python manage.py migrate
docker exec -it 261e658273912affcde5af python manage.py createsuperuser
```

## About this project
The project has following endpoints

- admin/
    * All the admin related tasks and DB handling can be done here
- product/all
    * Get all available product. This endpoint does not need admin privilege. But currently need admin permission.
- product/add
    * This endpoint is to add new product. This is for fully admin endpoint.
- product/<int:pk>
    * To view a product's information
- product/modify/<int:pk>
    * To edit the or delete the product data. Admins only task
- cart/add
    * This endpoint is for local users. Here a user can add products into his/her personal cart 
- cart/all
    * List all items added to the cart.
- cart/<int:pk>
    * This is to check a single product in the cart
- user/add:
    * Create a new local user can be done here.

### I allocated time in following ways to manage 8 hours.
- Understand what is needed for this project : approx. 60 minutes
- To plan the project (To plan the needed endpoints and needed packages, Read some documentations): approx. 120 minutes
- Design the endpoints: approx. 45 minutes
- Model design the contents: approx. 45 minutes 
- Develop Django Application: approx. 120 minutes
- Test the application: approx: 30 minutes
- Containerize the application: approx. 30 minutes
- Testing the containerized application: approx. 30 minutes
