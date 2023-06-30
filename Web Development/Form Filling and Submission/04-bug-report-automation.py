from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Specify the URL of the bug report form
bug_report_url = "https://example.com/bug-report"

# Specify the bug details
bug_title = "Bug Title"
bug_description = "Bug Description"
bug_priority = "High"

# Set up the Selenium WebDriver
driver = webdriver.Chrome()  # Update with the appropriate webdriver for your browser

# Open the bug report form
driver.get(bug_report_url)

# Fill in the bug details
title_field = driver.find_element_by_id("bug-title-input")  # Update with the ID or CSS selector of the title input field
title_field.send_keys(bug_title)

description_field = driver.find_element_by_id("bug-description-input")  # Update with the ID or CSS selector of the description input field
description_field.send_keys(bug_description)

priority_field = driver.find_element_by_id("bug-priority-select")  # Update with the ID or CSS selector of the priority select field
priority_field.send_keys(bug_priority)

# Submit the bug report
submit_button = driver.find_element_by_id("submit-button")  # Update with the ID or CSS selector of the submit button
submit_button.click()

# Close the browser
driver.quit()

