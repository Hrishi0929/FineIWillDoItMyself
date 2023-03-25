# we're saying from flask import flask
# so we are importing this flask class and then we're creating this
# app variable and setting this to
# an instance of this flask class now passing in
# the double underscore name can seem a bit confusing
# double underscore name is a special
# variable in python that is just the name of the module
# now if we run the script with python directly
# then double underscore name can be equal to
# double underscore main and we'll see that in just a second
# basically that is so flask knows where to look for
# your templates and static files and things like that

from flask import Flask

## this creates a WSGI application which is a standard that is actually used to communicate between the web server and the web application
app = Flask(__name__)

# basically decorators are just a way to add additional functionality
# to existing functions and in this case this
# app.route decorator will handle all of the complicated
# backend stuff and simply allow us to
# write a function that returns the
# information that will be shown on our website
# for this specific route so this forward slash here
# is just the root page of our website or
# you can think of it as the home page
# and we are simply returning the text "Welcome to the machine"


## this is the decorator it comes with a binding along with the function
@app.route("/")
def welcome():
    return "Welcome to the machine."


## this is the decorator it comes with a binding along with the function
@app.route("/PinkFloyd")
def pinkFloyd():
    return "Another Brick In the Wall..."


if __name__ == "__main__":
    ## debug = True keeps restarting the server when we save the code.
    app.run(debug=True)
