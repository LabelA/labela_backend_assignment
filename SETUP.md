Task Description: [README.md](README.md)

## Table of Contents:

* [Getting Started](#getting-started)
    * [Prerequisites](#prerequisites)
    * [Steps To Run](#steps-to-run)
* [Configuration](#configuration)
* [Considerations](#considerations)
* [Possible Improvements](#possible-improvements)
* [Contact](#contact)

## Getting Started:

Instructions on how to setup the project, its requirements and things to note during development:

### Prerequisites:

- Docker 4.11.0
- Docker Compose 2.7.0

#### Steps to run:

- ###### Install Prerequisites
    - Install Docker
    - Install Docker Compose

- ###### Setup the docker environment
    - Open terminal
    - Run Docker Container
      `docker compose up -d`

- ###### Test APIs
    - Access Django Admin
      `username: admin | password: admin`
    - Access APIs via Swagger
      `http://127.0.0.1:8000/swagger`
    - Authorize user to access API with admin credentials:
      `username: admin | password: admin`
    - Play around with APIs on Swagger

#### API List:

- Product Listing: [GET] `/api/v1/inventory/products`
- Product Detail: [GET] `/api/v1/inventory/products/<product_id>`
- Create Cart: [POST] `/api/v1/storefront/cart/`
- View Cart: [POST] `/api/v1/storefront/cart/<cart_id>`
- Add Item to Cart: [POST] `/api/v1/storefront/cart/<cart_id>/entries/`
- View Cart Item: [GET] `/api/v1/storefront/cart/<cart_id>/entries/<entry_id>`
- Update Cart Item: [PUT] `/api/v1/storefront/cart/<cart_id>/entries/<entry_id>`
- Delete Cart Item: [DELETE] `/api/v1/storefront/cart/<cart_id>/entries/<entry_id>`
- Checkout Cart: [DELETE] `/api/v1/storefront/cart/<cart_id>/checkout`

#### Possible Improvements:

- Add JWT based user authentication for APIs
- Add user permissions for cart and order APIs
- Improve admin interface with inline fields
- Improve unit test coverage
- Improve documentation
- Expose APIs to create brands and products
- Allow capability to atomically increment/decrement cart quantity
- Improve exception handling and global handlers
- Add FSM(Finite State Machine) based workflow for order management
- Improve DB schema and performance with Indexes and Constraints

### Contact

[@Nitin Sachdev](https://www.linkedin.com/in/nitin-sachdev) : nitin_sachdev@outlook.com

