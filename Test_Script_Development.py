from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.quit()

# 1. Login and Logout Functionality
def test_login_logout(driver):
    driver.get("https://demo-opencart.com/index.php?route=common/home&language=en-gb")
    time.sleep(7)
    
    driver.find_element(By.XPATH, "//*[@id='top']/div/div[2]/ul/li[2]/div/a").click()
    time.sleep(7)  
    driver.find_element(By.CSS_SELECTOR, "a.dropdown-item[href*='route=account/login']").click()
    time.sleep(7)
    # Login
    driver.find_element(By.ID, "input-email").send_keys("abc@gmail.com")
    driver.find_element(By.ID, "input-password").send_keys("12345")
    driver.find_element(By.XPATH, "//*[@id='form-login']/div[3]/button").click()
    # Validate login success or failure
    time.sleep(7)
    # Logout
    driver.find_element(By.XPATH, "//*[@id='top']/div/div[2]/ul/li[2]/div/a").click()
    time.sleep(7)
    # Quá trình đăng xuất
    driver.find_element(By.CSS_SELECTOR, "a.dropdown-item[href*='route=account/logout']").click()
    time.sleep(7)


# 2. Form Submission Functionality
def test_form_submission(driver):
    
    driver.get("https://demo-opencart.com/index.php?route=account/login&language=en-gb")
    time.sleep(3)
    # Fill out form
    driver.find_element(By.ID, "input-email").send_keys("abc@gmail.com")
    driver.find_element(By.ID, "input-password").send_keys("12345")
    time.sleep(3)
    driver.find_element(By.XPATH, "//*[@id='form-login']/div[3]/button").click()
    # Check for submission success message
    time.sleep(3)
    

# 3. Navigation Functionality
def test_navigation(driver):
    driver.get("https://demo-opencart.com/index.php?route=account/login&language=en-gb")
    #Login
    driver.find_element(By.ID, "input-email").send_keys("abc@gmail.com")
    driver.find_element(By.ID, "input-password").send_keys("12345")
    time.sleep(3)
    driver.find_element(By.XPATH, "//*[@id='form-login']/div[3]/button").click()
    time.sleep(7)
    driver.find_element(By.XPATH, "//span[@class='d-none d-md-inline' and text()='Wish List (0)']").click()
    time.sleep(7)
    assert "My Wishlist" in driver.title
    time.sleep(7)
    driver.find_element(By.XPATH, "//span[@class='d-none d-md-inline' and text()='Shopping Cart']").click()
    time.sleep(7)
    assert "Shopping Cart" in driver.title

# 4. Data Validation Functionality
def test_data_validation(driver):
    driver.get("https://demo-opencart.com/index.php?route=common/home&language=en-gb")
    time.sleep(7)
    
    #Check name
    product_names = driver.find_element(By.XPATH, "//a[text()='MacBook']")
    assert product_names.text == "MacBook", "No Products names found!"
    
    #Check price
    product_prices_element = driver.find_element(By.XPATH, "//*[@id='content']/div[2]/div[1]/div/div[2]/div/div/span[1]")
    prodct_price = product_prices_element.text.split("\n")[0]
    assert prodct_price == "$602.00", "Price is not correct!"
    
    #Check description
    product_descriptions_element = driver.find_element(By.XPATH, "//div[@class='description']/p")
    product_descriptions = product_descriptions_element.text
    
    except_description = "Intel Core 2 Duo processor"
    
    assert except_description in product_descriptions, "Description is not correct!"
    
    print("Data validation passed!")
    
    
    

# 5. Add to Cart and Checkout Functionality
def test_add_to_cart_and_checkout(driver):
    driver.get("https://demo-opencart.com/index.php?route=account/login&language=en-gb")
    time.sleep(3)
    
    #Login
    driver.find_element(By.ID, "input-email").send_keys("abc@gmail.com")
    driver.find_element(By.ID, "input-password").send_keys("12345")
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()
    time.sleep(7)
    
    driver.get("https://demo-opencart.com/")
    time.sleep(7)
    
    # Add item to cart
    driver.find_element(By.XPATH, "//*[@id='content']/div[2]/div[1]/div/div[2]/form/div/button[1]").click()
    time.sleep(7)
    
    # Go to cart and proceed to checkout
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-lg.btn-inverse.btn-block.dropdown-toggle").click()
    time.sleep(7)
    driver.find_element(By.XPATH, "//*[@id='header-cart']/div/ul/li/div[2]/p/a[3]").click()
    time.sleep(7)
    
    #Checkout
    driver.find_element(By.XPATH, "//*[@id='button-payment-methods']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='input-payment-method-bank_transfer-bank-transfer']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='button-payment-method']").click()
    time.sleep(2)
    driver.find_element(By.NAME, "comment").click()
    time.sleep(2)
    driver.find_element(By.NAME, "comment").send_keys("abcdef")
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='button-confirm']").click()
    time.sleep(2)
    
    

     
    assert "Checkout" in driver.title

# # 6. Search Functionality
def test_search(driver):
    driver.get("https://demo-opencart.com/index.php?route=common/home&language=en-gb")
    time.sleep(7)
    # Perform search
    driver.find_element(By.NAME, "search").send_keys("Macbook")
    time.sleep(7)
    
    # Validate search results
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-light.btn-lg").click()
    time.sleep(7)
    assert "Search - Macbook" in driver.title
    

# # 7. Responsive Design Functionality
def test_responsive_design(driver):
    driver.get("https://demo-opencart.com/index.php?route=common/home&language=en-gb")
    
    # Resize for different screen sizes
    for width, height in [(1024, 768), (768, 1024), (375, 667)]:
        driver.set_window_size(width, height)
        time.sleep(3)
        assert "menu" in driver.page_source, "Responsive design check failed for size: {}x{}".format(width, height)

