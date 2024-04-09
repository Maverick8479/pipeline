from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

# Set up the driver (assuming you are using Chrome)

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=options)
# Open the HTML file
driver.get("file:////var/www/html/index.html")

# Find the search input element
search_input = driver.find_element_by_id("search")

# Enter a search term
search_term = "After"
search_input.send_keys(search_term)

# Simulate pressing Enter
search_input.send_keys(Keys.RETURN)

# Wait for the search results to load
time.sleep(5)

# Check if the search term is found in the results
# This example assumes that search results are displayed in an element with id "results"
# You may need to adjust this based on how your application displays search results
try:
    results = driver.find_element_by_id("results")
    if search_term in results.text:
        print("Test Passed")
    else:
        print("Test Failed: Search term not found in results")
except Exception as e:
    print(f"Test Failed: {e}")

# Close the driver
driver.quit()
