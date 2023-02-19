from flask import Flask, request, jsonify
import util
app = Flask(__name__)

@app.route('/get_locations_names', methods=['GET'])
def get_locations_names():
    response = jsonify({
        'locations' : util.get_locations_names()
    })
    response.headers.add("Access-Control-Allow-Origin",'*')
    return response

@app.route('/predict_house_price', methods = ['GET','POST'])    
def predict_house_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location,total_sqft,bhk,bath)
    })
    response.headers.add('Access-Control-Allow-Design','*')

    return response

if __name__ == "__main__":
    print("Starting flask server for House price prediction")
    util.load_saved_artifacts()
    app.run()