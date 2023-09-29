from appium import webdriver
from selenium.webdriver.common.by import By
import pytest

desired_cap ={
    "platformName": "Android",
    "deviceName": "Android Emulator",
    "platformVersion": "9.0",
    "appPackage": "com.example.myapp",
    "appActivity": ".MainActivity",
    "automationName": "UiAutomator2"
}


driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
driver.implicitly_wait(30)

# close the popup
driver.find_element(By.ID,"com.flipkart.android:id/btn_skip").click()

# Get the price of the first laptop and verify the price
driver.find_element(By.XPATH,"//android.widget.ImageButton[@content-desc='Drawer']").click()
driver.find_element(By.XPATH,"//android.widget.TextView[@text='Electronics']").click()
driver.find_element(By.XPATH,"//android.widget.TextView[@text='Laptops']").click()
driver.find_element(By.ID,"com.flipkart.android:id/tv_card_view_holder").click()
driver.find_element(By.ID,"com.flipkart.android:id/not_now_button").click()

# Get the price and assert
price = driver.find_element(By.XPATH,"//android.widget.TextView[@bounds='[226,475][339,509]']").get_attribute("text")
print("The first mobile price value is " + price)
assert price == "₹68,999", "The price is not matched"