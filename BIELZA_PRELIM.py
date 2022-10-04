import json
from flask import Flask, jsonify, request

app = Flask(__name__)
temperature = [
    {
        "temp_id":"1",
        "date":"October 4, 2022",
        "temperature":"29 Celsius"
    }
]

@app.route('/temperature', methods=['GET'])
def readTemp():
    return jsonify(temperature)

@app.route('/temperature/<string:temp_id>')
def getTemp(temp_id):
    for temp in temperature:
        if (temp['temp_id']==temp_id):
            return jsonify(temperature)
    return jsonify({'message':'temp_id not found'})

@app.route('/temperature', methods=['POST'])
def addTemp():
    temp = request.get_json()
    temperature.append(temp)
    return{'temp_id': len(temperature)},200

@app.route('/temperature/<int:index>', methods=['DELETE'])
def deleteTemp(index):
    temperature.pop(index)
    return 'Temperature was deleted successfully', 200

if __name__ == '__main__':
    app.run()