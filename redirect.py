#to redirect user to other endpoint use the redirect() func
#to abort a req early with an error code use the abort() func

from flask import abort, redirect, url_for, Flask

redirect = Flask(__name__)

@redirect.route('/')
def index():
    return redirect(url_for('login')) #url_for gen the url for login route

@redirect.route('/login')
def login():
    abort(401)
    this_is_never_executed() #this func will not b exec coz abort terminates

if __name__ == '__main__':
    redirect.run(debug=True)
