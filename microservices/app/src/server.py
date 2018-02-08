from src import app
from flask import jsonify, json
from flask import Flask,render_template,make_response
import requests

@app.route("/")
def home():
    return "Hasura Hello World"

@app.route("/hello")
def hello_world():
	return "Hello World - Thiru"
# Uncomment to add a new URL at /new

@app.route("/json")
def json_message():
    return jsonify(message="Hello World")
	
@app.route("/getmetric")
def get_metric():
	#query to select the data from the table
	
# This is the url to which the query is made
	url = "https://data.declassification29.hasura-app.io/v1/query"

	# This is the json payload for the query
	requestPayload = {
		"type": "select",
		"args": {
			"table": "world_happiness_report",
			"columns": [
				"*"
			],
			"order_by": [
				{
					"column": "ID"
				}
			]
		}
	}

	# Setting headers
	headers = {
		"Content-Type": "application/json"
	}

	# Make the query and store response in resp
	resp = requests.request("POST", url, data=json.dumps(requestPayload), headers=headers)

	# resp.content contains the json response.
	return resp.content
	


