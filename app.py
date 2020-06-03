
# # model = app.model('Prediction params', 
# # 				  {'select4': fields.String(required = True, 
# # 				  							   description="select4", 
# #     					  				 	   help="select4 cannot be blank"),
# # 				  'select5': fields.String(required = True, 
# # 				  							   description="select5", 
# #     					  				 	   help="select5 cannot be blank"),
# # 				  'select1': fields.String(required = True, 
# # 				  							description="Select 1", 
# #     					  				 	help="Select 1 cannot be blank"),
# # 				  'select2': fields.String(required = True, 
# # 				  							description="Select 2", 
# #     					  				 	help="Select 2 cannot be blank"),
# # 				  'select3': fields.String(required = True, 
# # 				  							description="Select 3", 
# #     					  				 	help="Select 3 cannot be blank"),
# # 				  'select6': fields.String(required = True, 
# # 				  							   description="select6", 
# #     					  				 	   help="select6 cannot be blank"),
# # 				  'select7': fields.String(required = True, 
# # 				  							   description="select7", 
# #     					  				 	   help="select7 cannot be blank"),
# # 				  'select8': fields.String(required = True, 
# # 				  							description="Select 8", 
# #     					  				 	help="Select 8 cannot be blank"),
# # 				  'select9': fields.String(required = True, 
# # 				  							description="Select 9", 
# #     					  				 	help="Select 9 cannot be blank"),
# # 				  'select10': fields.String(required = True, 
# # 				  							description="Select 10", 
# #     					  				 	help="Select 10 cannot be blank"),
# # 				  'select11': fields.String(required = True, 
# # 				  							description="Select 11", 
# #     					  				 	help="Select 11 cannot be blank"),
# # 				  'select12': fields.String(required = True, 
# # 				  							description="Select 12", 
# #     					  				 	help="Select 12 cannot be blank")})

# # weights = torch.load('/home/fuhrer/Desktop/Placement-analysis/data/classifier')
# # def predict(arr):
# # 	y = np.dot(weights['linear.weights'].to_numpy(),arr) + weights['linear.bias']
# # 	if(y>=0.5):
# # 		return 1
# # 	else:
# # 		return 0


from flask import Flask, request, jsonify, make_response
from flask_restplus import Api, Resource, fields
from sklearn.externals import joblib
import numpy as np
import sys

flask_app = Flask(__name__)
app = Api(app = flask_app, 
		  version = "1.0", 
		  title = "Iris Plant identifier", 
		  description = "Predict the type of iris plant")

name_space = app.namespace('prediction', description='Prediction APIs')

# model = app.model('Prediction params', 
# 				  {'sepalLength': fields.Float(required = True, 
# 				  							   description="Sepal Length", 
#     					  				 	   help="Sepal Length cannot be blank"),
# 				  'sepalWidth': fields.Float(required = True, 
# 				  							   description="Sepal Width", 
#     					  				 	   help="Sepal Width cannot be blank"),
# 				  'petalLength': fields.Float(required = True, 
# 				  							description="Petal Length", 
#     					  				 	help="Petal Length cannot be blank"),
# 				  'petalWidth': fields.Float(required = True, 
# 				  							description="Petal Width", 
#     					  				 	help="Petal Width cannot be blank")})

# classifier = joblib.load('classifier.joblib')

@name_space.route("/")
class MainClass(Resource):
# formData = request.json
			# data = [val for val in formData.values()]
			# prediction = classifier.predict(np.array(data).reshape(1, -1))
	# def options(self):
	# 	response = make_response()
	# 	response.headers.add("Access-Control-Allow-Origin", "*")
	# 	response.headers.add('Access-Control-Allow-Headers', "*")
	# 	response.headers.add('Access-Control-Allow-Methods', "*")
	# 	return response

	# @app.expect(model)		
	def post(self):
		try: 
			# formData = request.json
			# data = [val for val in formData.values()]
			# prediction = classifier.predict(np.array(data).reshape(1, -1))
			types = { 0: "Iris Setosa", 1: "Iris Versicolour ", 2: "Iris Virginica"}
			response = jsonify({
				"statusCode": 200,
				"status": "Prediction made",
				"result": "The type of iris plant is: jhvjh"
				})
			response.headers.add('Access-Control-Allow-Origin', '*')
			return response
		except Exception as error:
			return jsonify({
				"statusCode": 500,
				"status": "Could not make prediction",
				"error": str(error)
			})




		 
