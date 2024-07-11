#to access cookies we use the cookies attribute.
'''the cookies attribute of request obj is a dict with alll the cookies the
client transmits.
Reading cookies:
'''
from flask import request

@app.route('/')
def index():
    username = request.cookies.get('username')
    #use cookies.get(key) instead of cookies[key] to not get a
    # keyError if the cookie is missing

#storing cookies
from flask import make_response

@app.route('/')
def index():
    resp = make_response(render_template(...))
    resp.set_cookie('username', 'the username')
    return resp
'''notable points for above code
cookies are set on the response objects
'''
