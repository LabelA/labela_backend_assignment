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


## Notes from One developer to another

#### Assumptions
Following assumptions were taken during the design and implementation stages:
- Minimum attributes to be used to denote the real world objects of the application.
- Credential storing best practices are not considered.
- Authentication and Authorization are not considered.

#### Approach notes
- Products, Customers, Orders, Carts were developed independantly for maximum code readability.
- API responses were paginated to 2 elements per call for demonstration purposes.
- Very small amount of seed data are introduced. (Will auto populate with docker-compose).

#### Run the project
Use `docker-compose up -d`
This will create the database, run the app and will be served at `http://127.0.0.1:8000/`

#### API documentation
Something went wrong last moment with swagger docs, so I unfortunately have to present you a Postman collection.
Import the Postman collection JSON named `LabelA_By_Sahan.postman_collection.json` at root of the project.

#### User Stories to API endpoints

| User Story | API Endpoint |
| ------ | ------ |
| As a company, I want all my products in a database, so I can offer them via our new platform to customers | GET /api/products/ |
| As a client, I want to add a product to my shopping cart, so I can order it at a later stage | POST /api/carts/ |
| As a client, I want to remove a product from my shopping cart, so I can tailor the order to what I actually need | DELETE /api/carts/ |
| As a client, I want to order the current contents in my shopping cart, so I can receive the products I need to repair my car | POST /api/orders/ |
| As a client, I want to select a delivery date and time, so I will be there to receive the order | PUT /api/orders/ |
| As a client, I want to see an overview of all the products, so I can choose which product I want | GET /api/products/ |
| As a client, I want to view the details of a product, so I can see if the product satisfies my needs | GET /api/products/ |

#### API calling flow
- Create Products   
    - POST /api/products/
- Get Products
    - GET /api/products/
- Get Product
    - GET /api/products/{id}/

- Create Customer (Creating a customer will automatically create a cart for the customer)
    - POST /api/customers/

- Put products to cart
    - PATCH /api/carts/{id}/
- Remove products from cart
    - DELETE /api/carts/1/remove_product/ 
    - Body must contain product id

- Create Order
    - POST /api/orders/
    - Body must contain cart id and delivery date time in ISO format ("2020-12-31T23:59:59Z")


#### Peronal Notes from the developer
- Best practices for API design were not followed due to time constraints.
- Swagger documentation was not implemented due to time constraints.
- Unit tests were not implemented due to time constraints.
