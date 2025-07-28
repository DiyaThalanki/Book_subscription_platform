import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module")
def driver():
    # You can set the path to chromedriver if not in PATH
    service = Service("./chromedriver.exe")  # or give full path: "C:/.../chromedriver.exe"
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

def test_end_to_end_register_and_browse(driver):
    driver.get("http://localhost:8501")

    # Wait for Streamlit to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "input"))
    )

    # Go to Register tab
    register_tab = driver.find_element(By.XPATH, "//button[.//p[text()='Register']]")
    register_tab.click()
    time.sleep(1)

    # Fill form
    email = f"e2e{int(time.time())}@test.com"
    driver.find_element(By.ID, "reg_email").send_keys(email)
    driver.find_element(By.ID, "reg_password").send_keys("password123")
    driver.find_element(By.XPATH, "//input[@type='password' and @placeholder='Confirm Password']").send_keys("password123")

    # Click register
    driver.find_element(By.XPATH, "//button[contains(text(),'Create Account')]").click()
    time.sleep(3)

    # Refresh page or rerun streamlit state
    driver.refresh()
    time.sleep(3)

    # Go to "Browse Books" page
    driver.find_element(By.XPATH, "//button[contains(text(),'Browse Books')]").click()
    time.sleep(2)

    # Try to click the first "Add to Library" button if available
    add_buttons = driver.find_elements(By.XPATH, "//button[contains(text(),'Add to Library')]")
    if add_buttons:
        add_buttons[0].click()
        time.sleep(2)

    # Check for success message
    alerts = driver.find_elements(By.CLASS_NAME, "stAlert")
    assert any("added" in alert.text.lower() for alert in alerts)
