#customization of the http error page can be done using errorhandler()decorator
from flask import render_template

@app.errorhandler(404)
def page_not_found(error):
    return render_template("page_not_found.html"), 404 

#the 404 after render temp call tells flask that the status code of that page 404
