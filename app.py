from flask import Flask, request, jsonify
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import time
import urllib.parse

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'message':'Hello Worldddddd!'})


@app.route('/test', methods=['POST'])
def scrape_data():
    return jsonify({'message':'Hello Worldddddd!'})
#   def scrape_data(username, password, url):
    # driver = None
   
    # try:
        
    #     data = request.json

    #     username = data['username']
    #     password = data['password']
    #     url = data['url']

    #     chrome_options = webdriver.ChromeOptions()
    #     chrome_options.add_argument("--user-data-dir=/path/to/a/{username}/profile")
    #     #use 
    #     # when running in a headless environment 
    #     chrome_options.add_argument("--no-sandbox") 
    #     chrome_options.add_argument("--headless")
    #     chrome_options.add_argument("--disable-gpu") 

    #     # # Set up the Selenium webdriver with the ChromeOptions
    #     driver = webdriver.Chrome(options=chrome_options)


    #     # Open LinkedIn
    #     driver.get("https://www.linkedin.com/")
    #     driver.set_page_load_timeout(15)
    #     time.sleep(4)  # Let the page load




    #     print("Linkdin page loaded................")
    #     print("entering credentials................")
       
        # current_url = driver.current_url
        # if "linkedin.com/feed/" in current_url:
        #     # logged in
        #     print("Already logged in")
        # else:
      
        #     print("Not logged in")
            
        #     # Perform the login process here (similar to your existing code)
        #     WebDriverWait(driver, 10).until(
        #         EC.visibility_of_element_located((By.NAME, "session_key"))
        #     )
        #     username_field = driver.find_element("name", "session_key")
        #     password_field = driver.find_element("name", "session_password")
        #     # Wait for the username field to be visible
        #     WebDriverWait(driver, 10).until(
        #         EC.visibility_of(username_field)
        #     )

        #     username_field.send_keys(username)
        #     password_field.send_keys(password)
        #     password_field.send_keys(Keys.RETURN)
        #     time.sleep(5)  # Let the login complete 
        #     print("logged in successfully.................")
    #     return jsonify({"message":"logged in successfully"})
    # except Exception as e:
    #     if driver is not None:
    #         driver.quit()
          
    #     return jsonify({"error":str(e)})
   




    
# if __name__ == '__main__':
#     app.run(debug=True, port=8080)