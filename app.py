from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os
from models import init_app

# pip install flask flask_sqlalchemy flask_cors

# app is created
app = Flask(__name__, static_folder='static', template_folder='templates')
CORS(app)
init_app(app)


app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


@app.route('/')
def home():
    return "Online Pharmacy API is running!"

# app is called
if __name__ == '__main__':
    app.run(debug=True)