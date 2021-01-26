from flask import Blueprint , request, render_template, make_response, jsonify
from model import logger
rest = Blueprint("rest", __name__ , url_prefix="/home")

@rest.route('/that',methods=['GET'])
def home():
    logger.logs()
    return make_response(jsonify({'Stata': True, 'msg': 'That'}), 200)