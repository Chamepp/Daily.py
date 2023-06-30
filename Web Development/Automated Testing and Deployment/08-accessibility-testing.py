from axe_selenium_python import Axe

from selenium import webdriver

# Set up the WebDriver (you can choose a different browser driver)
driver = webdriver.Chrome()

# Navigate to the web page you want to test
driver.get("https://example.com")

# Create an instance of the Axe accessibility scanner
axe = Axe(driver)
axe.inject()

# Run the accessibility scan
results = axe.run()

# Check if there are any violations
if results["violations"]:
    print("Accessibility violations found:")
    for violation in results["violations"]:
        print("- Rule: ", violation["id"])
        print("  Description: ", violation["description"])
        print("  Help: ", violation["helpUrl"])
else:
    print("No accessibility violations found.")

# Close the browser
driver.quit()

