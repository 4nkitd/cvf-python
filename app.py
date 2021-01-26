import json, os
from dotenv import load_dotenv, find_dotenv
from flask import Flask, request, render_template, make_response, jsonify

# import controllers
from controller.rest import rest

# call all required functions 
load_dotenv(find_dotenv())
app = Flask(__name__)

# Example Code Block
""" 
os.getenv("EMAIL") 

"""

# connecting controller
app.register_blueprint(rest)

# exaample route
@app.route('/', methods=['GET'])
def hello_world():
    return 'Page Not Found On ' + os.getenv("HOST")

# custom 404 error handler
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'Stata': False, 'msg': 'Not found'}), 404)


# custom 400 error handler
@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'Stata': False, 'msg': 'Bad request'}), 400)

# 
if __name__ == "__main__" :
 
    host = os.getenv("HOST") 
    port = os.getenv("PORT") 
    debug = os.getenv("DEBUG")

    app.run(host=host,port=port,debug=debug)