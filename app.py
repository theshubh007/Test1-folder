
from flask import Flask, request, jsonify, render_template,json,current_app
from flask_restful import Resource, Api
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import urllib.parse



app = Flask(__name__)


@app.route('/')
def home():
    return jsonify({'message':'Hello World!'})








    
# if __name__ == '__main__':
#     app.run(debug=True, port=8080)