import sys
import time

from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def loginOAuth(interactive):

	# 1. get auth button and click
	buttons = driver.find_elements("xpath", ".//button")
	authorizeButton = None
	for button in buttons:
		if (button.text == "Authorize"):
			authorizeButton = button
	authorizeButton.click()

	if (interactive):
		time.sleep(delay) # Allow the user to see what is going on...

	# 2. get 'select all' and click
	selectAllButton = driver.find_element(By.XPATH, "//*[contains(text(), 'select all')]")
	selectAllButton.click()

	if (interactive):
		time.sleep(delay) # Allow the user to see what is going on...

	# 3. get auth button and click
	buttons = driver.find_elements("xpath", ".//button")
	authorizeButton = None
	for button in buttons:
		if (button.text == "Authorize"):
			authorizeButton = button
	authorizeButton.click()

	# 4. look for sign-in window, fill in u/p snd sign-in
	time.sleep(delay) # Get time to load the page...
	window_after = driver.window_handles[1]
	driver.switch_to.window(window_after)

	usernameTxtField = driver.find_element(By.XPATH, "//input[@placeholder='Username']")
	passwordTxtField = driver.find_element(By.XPATH, "//input[@placeholder='Password']")

	usernameTxtField.send_keys("u")
	passwordTxtField.send_keys("p")

	signInButton = driver.find_element(By.XPATH, "//*[contains(text(), 'Sign in')]")
	signInButton.click()

	time.sleep(delay) # Get time to load the page...

	# 5. Is consent requested, i.e. is the second window still up?
	if (len(driver.window_handles) == 2): 
		driver.find_element(By.ID, "product:write").click();
		driver.find_element(By.ID, "product:read").click();
		driver.find_element(By.ID, "submit-consent").click();
	
	# 6. back to Swagger UI window")
	time.sleep(delay) # Get time to load the page...
	window_after = driver.window_handles[0]
	driver.switch_to.window(window_after)

	# 7. click on the close button
	closeButton = driver.find_element(By.XPATH, "//*[contains(text(), 'Close')]")
	closeButton.click()

print ("Running OpenAPI Web UI tests...")

performLogin = False
if "login" in sys.argv:
	performLogin = True

interactive = False
if "interactive" in sys.argv:
	interactive = True

if interactive:
    delay = 3
else:
    delay = 1

print ("Interactive={0}, Delay={1} seconds".format(interactive, delay))

url = 'http://localhost:8080/openapi/swagger-ui.html'
if (performLogin):
	url = 'https://localhost:8443/openapi/swagger-ui.html'

options = Options()
if not interactive:
    options.add_argument("--headless=new")
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

driver.get(url) 
time.sleep(delay) # Get time to load the page...

if interactive:
	print ("Press Return to start the tests!")
	i = input()

if (performLogin):
	loginOAuth(interactive)

# 1. Find the GET button and click it
getButton = driver.find_element("xpath", ".//button[@aria-label='get \u200b/product-composite\u200b/{productId}']")
getButton.click()

# 2. Find the 'Try it out' button and click it
time.sleep(delay) # Get time to load the page...
tryButton = driver.find_element(By.XPATH, ".//button[contains(text(), 'Try it out')]")
tryButton.click()

# 3. Find the input field for productId and fill it in
productIdTxtField = driver.find_element(By.XPATH, "//input[@placeholder='productId']")
productIdTxtField.send_keys('1')

# 4. Execute the query
execButton = driver.find_element(By.XPATH, ".//button[contains(text(), 'Execute')]")
execButton.click()

# 5. Find the respose code and body
time.sleep(delay) # Get time to load the page...

responseTr = driver.find_element(By.CLASS_NAME, "response")
responseTds = responseTr.find_elements("xpath", ".//td")
codeTd = responseTds[0]
bodyTd = responseTds[1]

# 6. Ok if code == 200 otherwise FAULT
if codeTd.accessible_name != "200":
	sys.exit("Expected 200, but got " + codeTd.accessible_name + ". \nResponse: " + bodyTd.accessible_name)

# 7. Ok if body contains '\"productId\": 1' otherwise FAULT
if not bodyTd.accessible_name.startswith("Response body Download { \"productId\": 1"):
	sys.exit("Expected '\"productId\": 1', but got " + codeTd.accessible_name + ". \nResponse: " + bodyTd.accessible_name)
else:
	print ("All OpenAPI Web UI tests ok!")

if interactive:
	print ("Press Return to wrap up the tests!")
	i = input()
