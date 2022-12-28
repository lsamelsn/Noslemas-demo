# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)


# this is called an endpoint or API
@app.route('/')
def hello_world():
    return 'Hello World'

if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(debug=True)


'''

Rest API's
CRUD (GET, POST, DELETE, PUT)

look up stuff to learn and definitions of it
-------------------
- do leetcode.com (easy)
    - it will teach you how to program a litte. some problems are dumb
- scraping tools (bs4, requests, selenium) <- tools for scraping
- sending API requests, helps with scraping and bots and debugging websites (postman)
- database for python (sqlite3)
    - database language (SQL)
- Rest API (flask)
- OOO progaming, classes
    - https://realpython.com/python3-object-oriented-programming/
- Algorithms and data strucutures
    -Algorithms
        - sorting
            - merge sort
            - quick sort
        - searching
            - linear search
            - binary search
    - data structures
        - arrays
        - linked lists
        - trees
        - stacks
        - queues

'''

