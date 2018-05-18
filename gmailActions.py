from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

loginEmail = "sheldonc3.14159@gmail.com"
loginPassword = ""
emailSubject = "Test Subject"
emailBody = "What's up!"
searchText = "test"
newLabelName = "My Stuff"

driver = webdriver.Chrome("/Users/stephcruz/Automation/Drivers/chromedriver")

# go to the google home page
driver.get("https://www.google.com/gmail/about/")

driverWait = WebDriverWait(driver, 20)

# Click the Sign In link
driver.find_element_by_css_selector(".gmail-nav > div > a:nth-child(2)").click()

# Enter email in text field
time.sleep(4)
driver.find_element_by_id("identifierId").send_keys(loginEmail)

# Click email Next button
driver.find_element_by_css_selector(".qhFLie > div > content.CwaK9 > span").click()

# Enter password in text field
time.sleep(4)
driver.find_element_by_css_selector("#password > div > div input").send_keys(loginPassword)

# Click password Next button
driver.find_element_by_id("passwordNext").click()

# If a captcha is displayed, print out a message
try:
    if driver.find_element_by_id(".Xb9hP > input#ca").is_displayed():
        print("Gmail requires a captcha to be entered.")

except NoSuchElementException:
    print("Continue test")

# Click the Compose button
time.sleep(6)
driver.find_element_by_css_selector(".aic > .z0 > div").click()

# Type an email in the To: field of the email
time.sleep(5)
driver.find_element_by_name("to").send_keys(loginEmail)
driver.find_element_by_name("to").send_keys(Keys.ENTER)

# Add a Subject to the email
driver.find_element_by_name("subjectbox").send_keys(emailSubject)

# Add text to email body
driver.find_element_by_css_selector(".Ap div:nth-child(2) > div").send_keys(emailBody)

# Click Send
driver.find_element_by_css_selector(".aDh > table > tbody > tr > td > div > .T-I").click()
time.sleep(4)

# Search for text
time.sleep(4)
driver.find_element_by_css_selector(".gsib_a > div > input:nth-child(1)").send_keys(searchText)
driver.find_element_by_css_selector("#gbqfbw > button").click()

# Delete email
time.sleep(5)
emailInInbox = driver.find_element_by_css_selector(".oZ-jc > .T-Jo-auh")
ActionChains(driver).context_click(emailInInbox).perform()
time.sleep(3)
driver.find_element_by_css_selector(".aDF").click()

# Click on the Inbox link
time.sleep(4)
driver.find_element_by_partial_link_text("Inbox").click()
time.sleep(4)

# Click on the email checkbox
driver.find_element_by_css_selector(".zA > td > div.oZ-jc > div").click()
time.sleep(3)

# Click the Move To button
driver.find_element_by_css_selector(".G-Ni > div:nth-child(1) > .asa > .ase").click()

# Click the Create New label button
time.sleep(3)
driver.find_element_by_css_selector("div.J-JK-Jz").click()

# Enter a label name
driver.find_element_by_css_selector("input.xx").send_keys(newLabelName)

# Click the Create button
driver.find_element_by_css_selector(".Kj-JD-Jl > button:nth-child(1)").click()

