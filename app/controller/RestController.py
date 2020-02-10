# Exposes RESTful endpoints for calling on model functions.
from flask import Flask
from flask import request
from app.model import BatterModel

app = Flask(__name__)


@app.route("/status")
def check_status():
    return "online"

# Given a batter name in the format first+last, and a pitcher name first+last, returns the probability a batter hits
@app.route('/hit', methods=['GET'])
def get_hit_probability():
    batter = request.args.get("batter")
    pitcher = request.args.get("pitcher")
    result = BatterModel.determine_hit_likelihood(batter, pitcher)
    print(result)
    return '{probability:' + str(123) + "}"
