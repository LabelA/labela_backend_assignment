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

# Project Setup Guidelines

#### Assumptions

- admin or superuser only can add, edit and delete the products.
- no login needed to view the product list and details of a product.
- login needed to add products into cart and to make orders.
- order quantity should be less than available stock.
- order delivery date cannot be in the past.
- user only can view their orders.
- admin can view list of orders.
- available stock will be deducted when user add to cart.
- available stock will be retained if user the cart.
- cart item will be cleared once made the order.

### Features covered

- user registration added.
- admin can add, edit and delete the products.
- any(unregistered) user can view the list of products.
- any(unregistered) user can view detail of a product.
- registered user only can add the product to cart.
- registered user only can delete the cart.
- registered user can make order with the cart content.
- registered user should mention the delivery date and time when make the order.

### Technologies Used

- Python Django framework
- Postgres db
- Django inbuilt ORM

#### To Setup and Start

- clone the repo
- run ```docker-compose build``` from root directory.
- run ```docker-compose up```
- login to the container with following command to create a superuser.
- ```docker exec -it labela_backend_assignment_web_1 /bin/bash```
- ```labela_backend_assignment_web_1``` is the container name, if it is different, change it accordingly.
- create a superuser by running following commands inside the container.
- ```python manage.py createsuperuser```
- give necessary inputs.
- Navigate to ```http://127.0.0.1/8000``` or ```http://localhost:8000/``` via a browser.
- you can use django rest framework inbuilt Web browsable API to make requests which is most user-friendly.

### Sample Requests, Responses for the features

Product
##### add products into db
 
- Login via Django Rest framework Web browsable API http://127.0.0.1:8000/api-auth/login by using created superuser.
- navigate to http://127.0.0.1:8000/product
- `{
        "product_code": "001",
        "product_name": "Fog Light",
        "unit_price": "10000.00",
        "available_stock": 50,
        "is_available": true,
        "description": "Toyota Fog Light",
        "type": "Lights",
        "company": "Toyota"
    }`
- make the POST request with above type of json.
- sample response will be like below.
- `{
        "id": 1,
        "product_code": "001",
        "product_name": "Fog Light",
        "unit_price": "10000.00",
        "available_stock": 50,
        "is_available": true,
        "description": "Toyota Fog Light",
        "type": "Lights",
        "company": "Toyota",
        "created": "2024-01-07T16:48:20.239962Z",
        "updated": "2024-01-07T16:48:20.239975Z"
    }`

##### edit/delete/get a product

- endpoint http://127.0.0.1:8000/product/001/
- 001 is a product_id

Cart
##### add a product to cart

- do register into the system.
- endpoint http://127.0.0.1:8000/register
- sample request body [POST]
- `{
    "username": "test_user1",
    "password1": "test_user1",
    "password2": "test_user1",
    "email": "test_user1@gmail.com"
  }`
- sample response "user registration success".
- login via http://127.0.0.1:8000/api-auth/login using above user.
- navigate to http://127.0.0.1:8000/cart endpoint.
- sample request body [POST]
- `{
    "product_code": "001",
    "quantity": 2
  }`
- sample response will be like below.
- `{
    "id": 1,
    "product_code": "001",
    "unit_price": "10000.00",
    "quantity": 2,
    "total_cost": "20000.00",
    "user": 2
  }`


##### delete/get a cart

- sample request endpoint http://127.0.0.1:8000/cart/1/
- 1 is a cart id.
- sample response
- `{
    "id": 1,
    "product_code": "001",
    "unit_price": "10000.00",
    "quantity": 2,
    "total_cost": "20000.00",
    "user": 2
  }`

Order
##### make an order with cart item

- request endpoint http://127.0.0.1:8000/order [POST]
- sample request
- `{
    "customer": "John",
    "email": "john@gmail.com",
    "phone": "+94773945782",
    "address": "Colombo",
    "delivery_date": "2024-01-30",
    "delivery_time": "10:30:00",
    "items": [
        {
            "id": 1,
            "product_code": "001",
            "unit_price": "10000.00",
            "quantity": 2,
            "total_cost": "20000.00",
            "user": 2
        }
    ]
  }`
- sample response
- `{
    "id": 1,
    "customer": "John",
    "email": "john@gmail.com",
    "phone": "+94773945782",
    "address": "Colombo",
    "status": "PENDING",
    "total_payment": "20000.00",
    "delivery_date": "2024-01-30",
    "delivery_time": "10:30:00",
    "created": "2024-01-07T18:19:50.317176Z",
    "updated": "2024-01-07T18:19:50.317187Z",
    "user": 2
  }`


#### Postman Collection
Product List

`curl --location --request GET 'http://127.0.0.1:8000/product' \
--header 'Cookie: csrftoken=DzkZ4iZErrk8uMS6wShaMFUdA9BcynA5R2fXEonbgjC9GpzDZ67gqf5ykYcCZZSG; sessionid=qur4cm64e704fory8f75covhgbpjbc2t'
`

Product

`curl --location --request GET 'http://127.0.0.1:8000/product/001' \
--header 'Cookie: csrftoken=DzkZ4iZErrk8uMS6wShaMFUdA9BcynA5R2fXEonbgjC9GpzDZ67gqf5ykYcCZZSG; sessionid=qur4cm64e704fory8f75covhgbpjbc2t'
`

Cart List

`curl --location --request GET 'http://127.0.0.1:8000/cart' \
--header 'Cookie: csrftoken=DzkZ4iZErrk8uMS6wShaMFUdA9BcynA5R2fXEonbgjC9GpzDZ67gqf5ykYcCZZSG; sessionid=qur4cm64e704fory8f75covhgbpjbc2t'
`

Cart

`curl --location --request GET 'http://127.0.0.1:8000/cart/1' \
--header 'Cookie: csrftoken=SZnSVF5n3WSFkkhVsVVWsg1LtcnJ9kG5neOnWmv6aoxuPREvDy1PxSIoWw2XCgCV; sessionid=qur4cm64e704fory8f75covhgbpjbc2t'
`

Order List

`curl --location --request GET 'http://127.0.0.1:8000/order' \
--header 'Cookie: csrftoken=SZnSVF5n3WSFkkhVsVVWsg1LtcnJ9kG5neOnWmv6aoxuPREvDy1PxSIoWw2XCgCV; sessionid=qur4cm64e704fory8f75covhgbpjbc2t'
`

Order

`curl --location --request GET 'http://127.0.0.1:8000/order/1' \
--header 'Cookie: csrftoken=SZnSVF5n3WSFkkhVsVVWsg1LtcnJ9kG5neOnWmv6aoxuPREvDy1PxSIoWw2XCgCV; sessionid=qur4cm64e704fory8f75covhgbpjbc2t'
`
