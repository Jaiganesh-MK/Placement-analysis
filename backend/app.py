from flask import request,jsonify,Flask,make_response
import dictionary as d
import numpy as np
import joblib

def pre_procession(data):
	data[0] = d.gender[data[0]]
	data[1] = d.tenth_p[data[1]]
	data[2] = d.board[data[2]]
	data[3] = d.tw_p[data[3]]
	data[4] = d.board[data[4]]
	data[5] = d.tw_s[data[5]]
	data[6] = d.ug_degree_p[data[6]]
	data[7] = d.fod[data[7]]
	data[8] = d.wr_exp[data[8]]
	data[9] = d.et_p[data[9]]
	data[10] = d.mba_s[data[10]]
	data[11] = d.mba[data[11]]
	return data

app = Flask(__name__)

model1 = joblib.load("rf.joblib")
model2 = joblib.load("nb.joblib")

@app.route("/predict",methods=["POST"])
def predict():

	if request.method=="POST":
		# request.headers.add('Access-Control-Allow-Origin', "*")
		formData = request.get_json()
		data = [val for val in formData.values()]
		data = pre_procession(data)
		dat = np.array(data)
		dat = dat.reshape(1,12)
		pred1 = model1.predict(dat)
		pred2 = model2.predict(dat)
		if(pred1==pred2):
			pred = pred1
		else:
			pred = pred2
		
		response = make_response()
		if pred == 0:
		 response = jsonify({"result":"NO"})
		else:
		 response = jsonify({"result":"YES"})
		# response.headers.add('Access-Control-Allow-Origin', '*')
		return response