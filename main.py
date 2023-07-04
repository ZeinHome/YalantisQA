import time
from selenium.webdriver.chrome.service import Service as ChromeService  
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def selenium_magic():
    print("Start Test")

    CHOROMEDRIVER_PATH = r'C:\Users\Ilya\OneDrive\Рабочий стол\YalantisQA\chromedriver.exe'
    service = ChromeService(executable_path=CHOROMEDRIVER_PATH) 
    driver = webdriver.Chrome(service=service)

  
    driver.get("https://rozetka.com.ua/")
    time.sleep(2)

    print("Enter query to search")
    search_input = driver.find_element(By.CSS_SELECTOR, "input[name='search']")
    search_input.send_keys('Xiaomi')
    search_input.send_keys(Keys.ENTER)

    time.sleep(2)
    print("Click on first item")
    driver.find_element(By.XPATH, ".//span[@class='goods-tile__title']/parent::a").click()

    time.sleep(2)
    print("Seacrh title and code")
    product_title = driver.find_element(By.CSS_SELECTOR, "h1.product__title")
    assert "Xiaomi" in product_title.text
    print("Good Title")
    product_code_element = driver.find_element(By.XPATH, ".//p[@class='product__code detail-code']")
    product_code = product_code_element.get_attribute("textContent").strip()
    assert product_code
    print("Good Code")

    time.sleep(2)

    driver.quit()
    print("end")


if __name__ == "__main__":
        selenium_magic()