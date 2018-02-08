from src import app
from flask import jsonify, json
from flask import Flask,request,render_template,make_response

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
