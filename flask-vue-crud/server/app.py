from flask import Flask, jsonify,request
from flask_cors import CORS
from datetime import datetime
from pytz import timezone, all_timezones_set,all_timezones
import json

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
# CORS(app, resources={r'/*': {'origins': 'http://localhost:8082'}})
CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/get_new_time', methods=['GET', 'POST'])
def convert_time():
    current_time = datetime.now().astimezone().strftime("%H:%M:%S %Z")
    return jsonify({
        'current_time': current_time,
        'time_zones' : list(all_timezones)
    })

@app.route('/get_timezone', methods=['GET'])
# @cross_origin(origin='*',headers=['Content- Type','Authorization'])
def get_new_time():
    tz = request.args.get('tz')
    current_time = datetime.now().astimezone(timezone(tz)).strftime('%H:%M:%S %Z')
    return jsonify({ 
        "current_time": current_time
    })

if __name__ == '__main__':
    app.run()