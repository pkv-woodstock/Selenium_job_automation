from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time


def abort_application():
    # Click close button
    close_button = driver.find_element(By.CLASS_NAME, value='artdeco-modal__dismiss')
    close_button.click()

    time.sleep(2)
    discard_button = driver.find_element(By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1]
    discard_button.click()


EMAIL = 'pkvstarscream@gmail.com'
PASSWORD = 'Pkv2509@2002'
PHONE = '9535819408'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(
    'https://www.linkedin.com/jobs/search/?currentJobId=3728439589&f_AL=true&geoId=102713980&keywords=machine%20learning%20engineer%20python&location=India&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true')

# click Sign in Button
time.sleep(2)
sign_in_button = driver.find_element(By.XPATH, value='/html/body/div[1]/header/nav/div/a[2]')
sign_in_button.click()

# sign in
time.sleep(5)
email = driver.find_element(By.NAME, value='session_key')
email.send_keys(EMAIL)
password = driver.find_element(By.NAME, value='session_password')
password.send_keys(PASSWORD)
sign_in_submit = driver.find_element(By.XPATH, value='//*[@id="organic-div"]/form/div[3]/button')
sign_in_submit.send_keys(Keys.ENTER)

# Easy apply
# time.sleep(7)


# Get listings
time.sleep(4)
all_listings = driver.find_elements(By.CSS_SELECTOR, value='.job-card-container--clickable')

# Apply for jobs
for listing in all_listings:
    print("Opening Listing")
    listing.click()
    time.sleep(2)
    try:
        # Click Apply Button
        easy_apply = driver.find_element(By.CSS_SELECTOR, value='.jobs-apply-button--top-card button')
        easy_apply.click()

        # Insert Phone Number
        time.sleep(5)
        phone_number = driver.find_element(By.ID,
                                           value='single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3728439589-99624989-phoneNumber-nationalNumber')
        if phone_number.text == "":
            phone_number.send_keys(PHONE)

        # check submit_button
        submit_button = driver.find_element(By.CSS_SELECTOR, value='footer button')
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            abort_application()
            print("Complex application, skipped.")
            continue
        else:
            print("Submitting job application")
            submit_button.click()

        time.sleep(2)
        # click close button
        close_button = driver.find_element(By.CLASS_NAME, value="artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        abort_application()
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()
