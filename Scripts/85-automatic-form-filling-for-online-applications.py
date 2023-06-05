from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Configure the webdriver (you need to install the appropriate driver for your browser)
driver = webdriver.Chrome("path_to_chromedriver")
driver.get("https://www.instagram.com")

# Wait for the page to load
time.sleep(2)

# Log in to Instagram (replace 'your_username' and 'your_password' with your actual credentials)
username = driver.find_element_by_name("username")
password = driver.find_element_by_name("password")
username.send_keys("your_username")
password.send_keys("your_password")
password.send_keys(Keys.ENTER)

# Wait for the login process to complete
time.sleep(5)

# Define the target Instagram profile
target_profile = "target_profile_username"

# Go to the target profile
driver.get("https://www.instagram.com/" + target_profile)

# Wait for the target profile to load
time.sleep(2)

# Scroll down the profile page to load more posts (adjust the range for more or fewer scrolls)
for _ in range(3):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

# Find all the post links on the profile page
post_links = driver.find_elements_by_xpath("//a[contains(@href, '/p/')]")

# Iterate through the post links and like and comment on each post
for post_link in post_links:
    driver.get(post_link.get_attribute("href"))
    
    # Wait for the post to load
    time.sleep(2)
    
    # Like the post
    like_button = driver.find_element_by_xpath("//button[@aria-label='Like']")
    like_button.click()
    
    # Add a comment to the post (replace 'Your comment here' with your desired comment)
    comment_input = driver.find_element_by_xpath("//textarea[@placeholder='Add a comment…']")
    comment_input.send_keys("Your comment here")
    comment_input.send_keys(Keys.ENTER)
    
    # Wait before moving on to the next post
    time.sleep(2)

# Close the browser
driver.quit()
