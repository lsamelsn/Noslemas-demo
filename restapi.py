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

'''

CRUD

GET

POST

DELETE

PUT

'''

if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(debug=True)