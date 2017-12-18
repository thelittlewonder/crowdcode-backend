from flask import Flask, render_template, request, jsonify
import cf_deployment_tracker
from flask_cors import CORS, cross_origin
import os
import json

# Emit Bluemix deployment event
cf_deployment_tracker.track()

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# On Bluemix, get the port number from the environment variable PORT
# When running this app on the local machine, default the port to 8000
port = int(os.getenv('PORT', 8000))

## work starts here

@app.route('/')
@cross_origin()
def home():
    return render_template('index.html')


# Returns the chapters and progress
@app.route('/api/chapters')
@cross_origin()
def chapters():
    return jsonify({
        "name":["Variables","Data Types","Conditionals","Arrays","Input and Output"],"lessons":[4,3,6,3,4],"quizzes":[3,2,4,3,5],"progress":[24,1,1,1,1]
    })

# Returns the leaderboard
@app.route('/api/leaderboard')
@cross_origin()
def leaderboard():
    return jsonify({
        1:["Deepika Sharma",345],2:["Nita Singh",325],3:["Pinky Agarwal",275],4:["Rita Gupta",230],5:["Sonia Goel",230],6:["Diksha Singh",225],7:["Pushpa Verma",195],8:["Nita Yadav",170],9:["Poonam Goyal",155],10:["Shelly Agrawal",130]
    })

# Returns the variables chapter content
@app.route('/api/variables')
@cross_origin()
def chapvariables():
    return jsonify({
        "summary":"In programming, a variable is a value that can change, depending on conditions or on information passed to the program. Typically, a program consists of instruction s that tell the computer what to do and data that the program uses when it is running.",
        "1":["Concept of Variables","What the eff are variables?","50","3"],
        "2":["Declaration","Take a new bowl from market!","1","2"],
        "3":["Defination","Make a dish and put it in the bowl.","1","5"],
        "4":["Recap","Use the bowl to store the dishes","1","3"],
    })

# Returns the variables chapter-1 content
@app.route('/api/variables/1')
@cross_origin()
def chapvariables1():
    return jsonify({
       "variable-1.svg":"Suppose you have a bowl and it contains hot soup. Here the container can be considered as a variable and the soup as the value, since it is stored in the bowl",
       "variable-2.svg":"You can change the contents of the bowl to a vegetable. So now the bowl contains vegetable, the value of the variable (bowl) is now updated.",
       "variable-3.svg":"Every variable will have a name. For example, we can have a variable named myBowl.",
       "summary":"A variable is a good way to store information while making it easy to refer to that information in our code later."
    })

# Returns the variables chapter-1 content
@app.route('/api/variables/2')
@cross_origin()
def chapvariables2():
    return jsonify({
       "variable-5.svg":"When you need a bowl, you go to the market to purchase one. Similarly, when we need a variable we have to ask the computer for one.",
       "variable-6.svg":"Since there are different types of bowls for different types of food. Similarly we have, different variable types for different data values.",
       "variable-7.svg":["To store integers, we generally use int data type, which is declared","which is analogous to saying to a shopkeeper, give me a bowl that can store integers and I will call it myNumber"],
       "variable-8.svg":["Similarly you can declare a variable to store words by using the keyword string.","Every variable is identified by its name, myName here. The same way, you use the color or other features to distinguish the bowl"],
       "summary":"First step of using a variable is to declare it, i.e purchasing the bowl from market to store food. Every variable has a name associated with it, which distinguishes it from other variables."
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)
