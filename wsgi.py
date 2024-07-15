from flask import Flask #this is a class in the flask module
app = Flask(__name__) #an instance of this class
'''the first arg is name of module __name__ is a convenient shortcut.
it is needed so that Flask knows where to look for resources such as
templates and static files.
'''

@app.route("/") #tells Flask what URL should trigger our func
def hello_world():
    return "<p>Hello, World!</p>"
# the func returns a html message we want to display in user's broswer
