# Setup Instructions
The application consists of the two directories: "frontend" and "backend".

The frontend directory contains a Vue application while the backend directory contains a Flask application.

## Setting up Flask backend
For the Flask application, change directory to the "backend" directory and create a virtual environment:

    python3 -m venv .venv
    . .venv/bin/activate

Then, install dependencies:
    
    pip install -r requirements.txt

Finally, from the same directory ("backend"), run the flask application:

    flask --app inventory run

## Setting up Vue frontend
For the Vue application, create a new terminal window and change directory to the "frontend/inventory" directory.

First, to install dependencies, run:

    npm install

Then to run the application, run:

    npm run dev

Click on the link that appears to open up the frontend application.

# Some things to note about the application
## Database
The database should already be populated with some dummy data. The database is located in the backend directory: backend/inventory.db

In case the data is not present for some reason, you can delete the inventory.db file, re-run the Flask application (which should instantiate a new inventory.db) and then navigate to the /management URL in the frontend, where you'll see a button to populate the database.

## Schema
The database schema might differ slightly from other submissions. There are 4 main tables/models:

Categories
Suppliers
Products
Inventory Items

Categories and Suppliers are simple structures. Products represent a certain type of product that may have some related categories. Inventory Items represent actual inventory, and link to a product and supplier. 

I did this since I thought certain inventory may be of the same product, but are supplied by various suppliers and have different purchase prices.

The main page is the Inventory page, which shows you all inventory items rolled-up by product. Clicking on one of the rows expands the row to display all individual inventory items of that product type.

Checkout backend/inventory/models.py to see the definitions of all the models mentioned.

# Technologies used and their justification
## Flask
I chose to use Flask since it is a relatively simple backend. Since I didn't have extensive experience in Flask or FastAPI, I thought Flask would have a gentler learning curve to get something up and running successfully.

## SQLAlchemy
I chose to use an ORM since it allows you to easily define and manipulate database schema in code. This can make things more maintainable and readable. It also lets us avoid writing raw SQL which can lead to various issues like possible SQL injection.

I chose SQLAlchemy for this simply because it is a well-established and popular Python ORM.

## SQLite
I chose SQLite since it is a simple and lightweight database with no configuration required.

## Vue
I chose to use Vue as my JS frontend framework because I am familiar with it, it is also relatively simple and powerful. Vue allowed me to manage state a lot better and create reusable components easily. 

## Tailwind
I utilized Tailwind in my application since it makes styling so easy and enjoyable.

# Things I would have changed
There are certain things that I would have liked to change or add given some more time.

## Server-side filtering
Right now, the application pulls all inventory items and then does filtering on the frontend. In a real-world scenario, this is not ideal due to the potentially massive amount of data being pulled from the DB. Ideally the backend application should have support to filter on categories, suppliers and products using URL query parameters.

## Pagination
Continuing with with the theme of backend filtering and limiting DB query sizes, pagination would have been great. This would have limited each query to a certain amount and also improved the UI experience. 

## Better error handling
Correct and consistent error handling on the frontend when querying the backend.

## Mobile-friendly
More effort into making the application's layout mobile-friendly.

## Selecting multiple objects for deletion
It would have been nice to be able to select multiple inventory items in order to mass-delete them.

I hope to hear how I did in the assessment, and wish you enjoy clicking around the app :D

All the best!
