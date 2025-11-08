import time
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import json


class WebUrlOzon:
    def __init__(self):
        options = Options()
        options.add_argument("--start-maximized")
        self.driver = uc.Chrome(options=options)
        self.driver.get("https://www.ozon.ru/")
        time.sleep(5)

    def search_product(self, query: str):
        search_box = self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Искать на Ozon']")
        search_box.send_keys(query)
        search_box.send_keys(Keys.ENTER)
        time.sleep(5)

    def extract_product_info(self):
        data = []
        time.sleep(5)

        products = self.driver.find_elements(By.CSS_SELECTOR, "div.tile-root")

        for product in products:
            try:
                title_elem = product.find_element(By.CLASS_NAME, "tsBody500Medium") 
                title = title_elem.text 
                href_elem = product.find_element(By.CLASS_NAME, "q4b1_3_0-a")
                
                price_elem = product.find_element(By.CLASS_NAME, "c35_3_11-a1") 
                price = price_elem.text #print(f"{title} | {price} | {href_elem.get_attribute('href')}")
                data.append({
                        "title": title,
                        "price": price,
                        "link": href_elem.get_attribute('href')
                    })

            except:
                continue

        return data

    def export_data(self, data):
        with open("ozon_products.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def close(self):
        self.driver.quit()


if __name__ == "__main__":
    ozon = WebUrlOzon()
    ozon.search_product("python books")
    data = ozon.extract_product_info()
    ozon.export_data(data)
    ozon.close()
