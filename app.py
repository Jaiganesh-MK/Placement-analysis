from flask import request,jsonify,Flask,make_response

app = Flask(__name__)

@app.route("/predict",methods=["POST"])
def predict():

	if request.method=="POST":
		# request.headers.add('Access-Control-Allow-Origin', "*")
		formData = request
		print(request.json)
		response = make_response()
		response = jsonify({"result":"sjs"})
		response.headers.add('Access-Control-Allow-Origin', '*')
		return response