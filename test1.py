import numpy as np
from flask import Flask, request, jsonify, render_template,json
import cv2
import requests
from skimage.metrics import structural_similarity as ssim
import pandas as pd
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
import urllib.parse
from selenium.webdriver.common.action_chains import ActionChains
import os


app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'message':'Hello World!'})

@app.route('/callchrome',methods=['POST'])
def predict():
   
    try:
        data = request.json

        username = data['username']
        password = data['password']
        ruffurl = data['url']

        print("Chrome driver initiated................")
        

        # chrome_options = webdriver.ChromeOptions()
        # chrome_driver_path = "/home/shubhppsu/mysite/chromedriver"
        # chrome_options.add_argument("--headless")
        # driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)

        # print("Chrome driver loaded................")
        # chrome_driver_path = "/home/shubhppsu/chrome_driver/chromedriver.exe"
        # chrome_options.add_argument("./chromedriver.exe=chromedriver")
        # driver = webdriver.Chrome(options=chrome_options)
        # driver = webdriver.Chrome() 

        chrome_options = webdriver.ChromeOptions() 
        chrome_options.add_argument("--no-sandbox") 
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu") 
        driver = webdriver.Chrome(options=chrome_options)

        # Open LinkedIn
        driver.get("https://www.linkedin.com/")
        driver.set_page_load_timeout(60)
        time.sleep(4)  # Let the page load




        print("Linkdin page loaded................")
       
        print("Linkdin page loaded................")
        username_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "session_key"))
        )
        password_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "session_password"))
        )
        # Wait for the username field to be visible
        WebDriverWait(driver, 10).until(
            EC.visibility_of(username_field)
        )

        username_field.send_keys(username)
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)
        time.sleep(5) 

        
            
        return jsonify({'status':format(driver.title)})

    except Exception as e:
        return jsonify({"error":str(e)})
    
if __name__ == '__main__':
    app.run(debug=True)