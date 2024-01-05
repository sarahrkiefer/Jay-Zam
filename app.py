import json
import os
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
from predict import predict
import subprocess

# Create App
app = Flask(__name__)

# Select Route
@app.route('/', methods=['POST', 'GET'])
@app.route('/index.html')
def index():
    return render_template("jay-zam.html")


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")