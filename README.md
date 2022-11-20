# Welcome to Django-Stripe!👋

Simple Django backend with Stripe integration.

# Quick start with Docker

1) Open `docker-compose.yml`
2) Edit:
  ```
    environment:
      - DJANGO_SECRET_KEY="Your Django Secret Key here" 
      - STRIPE_PUBLIC_API_KEY="Your Stripe Publishable Key here"
      - STRIPE_API_KEY="Your Stripe Private Key here"
  ```
   
3) `docker compose up --build` in your terminal

4) `http://localhost:8000/` in your Browser

Admin user and test instances should already be created. 


# Documentation

## Routes 

1) GET `item/{id}` 
    - Provides information about given item such as name, description and price
    - Provides an opportunity to buy item using Stripe payment API

2) GET `order/{id}`
    - Provides information about all items in given order.
    - Provides an opportunity to buy all the items using Stripe payment API

## Stripe integration 

Custom API Client is implemented in `app.api.payment_api.py`.

When a user clicks on "Buy" button, the following processes start:
    - If `stripe_id` field is empty for given Item instance(`app.core.models.py`), then a request is being sent to Stripe in order to receive a sid(Stripe id) of `Product` Stripe instance 
    - If `stripe_id` field of `Price` object asigned to given `Item` is empty, then the request is being sent to Stripe in order to receive a sid(Stripe id) of `Price` Stripe instance (Which is basically main instance when creating `Stripe.checkout.session`)
    - A request is being sent in order to receive an ID of Stripe Checkout Session and if the request was successful - a user is being redirected to payment page, otherwise, the user is alerted that an error ocurred 

## Syncronizing Stripe and Django instances 

When django instance is being changed, a new Stripe Product needs to be created. For this purpose, two custom signals are implemented in `app.core.models.py`:
    - When an instance of either `Item` or `Price` is changed, `stripe_id` field is removed, thus next time when a user clicks on Buy button - a request to Stripe will be sent to create new instances.


## Administration 

Basic Django Admin functionality is added to the project. When you start the project using docker, it automatically creates a superuser instance. You can check the credentials in `app.core.management.commands.create_admin.py`
 







