
from flask import Flask, request, jsonify, render_template,json,current_app
from flask_restful import Resource, Api
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
api = Api(app)

@app.route('/')
def home():
    return jsonify({'message':'Hello World!'})



@app.route('/callchrome',methods=['POST'])    
def scrape_data():
#   def scrape_data(username, password, url):
    driver = None
   
    try:
        data = request.json

        username = data['username']
        password = data['password']
        url = data['url']

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--user-data-dir=/path/to/a/{username}/profile")
        #use 
        # when running in a headless environment 
        # chrome_options.add_argument("--no-sandbox") 
        # chrome_options.add_argument("--headless")
        # chrome_options.add_argument("--disable-gpu") 

        # # Set up the Selenium webdriver with the ChromeOptions
        driver = webdriver.Chrome(options=chrome_options)


        # Open LinkedIn
        driver.get("https://www.linkedin.com/")
        driver.set_page_load_timeout(15)
        time.sleep(4)  # Let the page load




        print("Linkdin page loaded................")
        print("entering credentials................")
       
        current_url = driver.current_url
        if "linkedin.com/feed/" in current_url:
            # logged in
            print("Already logged in")
        else:
      
            print("Not logged in")
            
            # Perform the login process here (similar to your existing code)
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.NAME, "session_key"))
            )
            username_field = driver.find_element("name", "session_key")
            password_field = driver.find_element("name", "session_password")
            # Wait for the username field to be visible
            WebDriverWait(driver, 10).until(
                EC.visibility_of(username_field)
            )

            username_field.send_keys(username)
            password_field.send_keys(password)
            password_field.send_keys(Keys.RETURN)
            time.sleep(5)  # Let the login complete    




      
        print("Login done................")
        print(driver.get_log('browser'))
        # Replace with the URL of the LinkedIn page you want to scrape
        ruffurl = "https://www.linkedin.com/search/results/people/?heroEntityKey=urn%3Ali%3Aorganization%3A1068&keywords=jpmorgan%20chase%20%26%20co.&origin=SWITCH_SEARCH_VERTICAL&position=8&searchId=1fb1705d-3e34-4995-b309-24b3be0ef7e3&sid=JfM"

        mainurl = urllib.parse.unquote(ruffurl)


        target_people_number=5

        totalNotConnectedProfiles = []
        totalConnectedProfiles = []
        url = mainurl
        driver.get(url)

        print("entered into loop................")
        print(driver.get_log('browser'))
        while True:
            if(len(totalNotConnectedProfiles)>=target_people_number):
                break
            
            time.sleep(4)
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".pv0.ph0.mb2.artdeco-card"))
            )
            print(driver.get_log('browser'))
            print("Company page loaded................")
            


            # Scroll down to load more content 
            num_scrolls = 5
            for _ in range(num_scrolls):
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                print(driver.get_log('browser'))
                time.sleep(2)

            # Get the page source
            page_source = driver.page_source
            print("page source loaded................")

            # Parse the page source with BeautifulSoup
            soup = BeautifulSoup(page_source, "html.parser")

            # Scraping Whole Profiles Lists
            all_profiles = soup.find_all("li", class_="reusable-search__result-container")
            profile_urls2 = []
            message_profiles = []
            non_message_profiles = []

            for profile in all_profiles:    
                button = profile.find("button", {"aria-label": "Message "})
                if button:
                    message_profiles.append(profile)
                else:
                    non_message_profiles.append(profile)
            

            finalProfileUrls = []
            print("Profiles without 'Message' button url collecting")
            for profile in non_message_profiles:
                url=profile.find("a", class_="app-aware-link")["href"]
                if(len(totalNotConnectedProfiles)>=target_people_number):
                    break
                finalProfileUrls.append(url)
                name_element = profile.select_one(".entity-result__title-text span span")
                name = name_element.get_text(strip=True) if name_element else "No Name Available"
                subtitle_element = profile.select_one(".entity-result__primary-subtitle")
                subtitle = subtitle_element.get_text(strip=True) if subtitle_element else "No Subtitle Available"
                print(name+" : "+subtitle)
            
                
            print("=====================================================")
            totalNotConnectedProfiles.extend(finalProfileUrls)

            buttons = driver.find_elements(By.CLASS_NAME,"artdeco-pagination__button")
            
            if buttons:
                button = buttons[1]
                if button.get_attribute("disabled"):
                    print("All pages finished, can't move to the next page")
                else:
                    button.click()
                    time.sleep(2)
            else:
                print("No buttons found")
                time.sleep(2)

        print("Total Not Connected Profiles: ", len(totalNotConnectedProfiles))
        for i in totalNotConnectedProfiles:
            print(i)    
        driver.quit()       
  
        return jsonify({"status": "success", "message": "Chrome driver initiated", "data": totalNotConnectedProfiles})
        

    except Exception as e:
        if driver is not None:
            driver.quit()
          
        return jsonify({"error":str(e)})
 
    




    
if __name__ == '__main__':
    app.run(debug=True, port=8080)