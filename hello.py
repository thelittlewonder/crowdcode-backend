from flask import Flask, render_template, request, jsonify
import cf_deployment_tracker
from flask_cors import CORS, cross_origin
import os
import json

# Emit Bluemix deployment event
cf_deployment_tracker.track()

db = None

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# On Bluemix, get the port number from the environment variable PORT
# When running this app on the local machine, default the port to 8000
port = int(os.getenv('PORT', 8000))

## work starts here

def load_database(filename='database.json'):
    global db
    with open(filename) as f:
        db = json.loads(f.read())


@app.route('/')
@cross_origin()
def home():
    return render_template('index.html')


# Returns the chapters and progress
@app.route('/api/chapters')
@cross_origin()
def chapters():
    return jsonify(db['chapters'])

# Returns the leaderboard
@app.route('/api/leaderboard')
@cross_origin()
def leaderboard():
    return jsonify(db['leaderboard'])

# Returns the variables chapter content
@app.route('/api/variables')
@cross_origin()
def chapvariables():
    return jsonify(db['variables']['all'])

# Returns the variables chapter-1 content
@app.route('/api/variables/1')
@cross_origin()
def chapvariables1():
    return jsonify(db['variables']['chapters']['1'])

# Returns the variables chapter-1 content
@app.route('/api/variables/2')
@cross_origin()
def chapvariables2():
    return jsonify(db['variables']['chapters']['1'])



if __name__ == '__main__':
    load_database()
    app.run(host='0.0.0.0', port=port, debug=True)
