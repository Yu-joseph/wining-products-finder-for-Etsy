from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import time

# # webdriver = webdriver.current_url("https:://etsy.com")
# # argv  = sys.argv
# i = 1
# # string = ""
# # if len(argv) == 1:
# #     print("please entry valid search title")
# #     exit()
# # else:
# #     while(i < len(sys.argv)):
# #         string += str(sys.argv[i])
# #         string += " "
# #         i += 
# keyword = input("Enter a keyword to search: ")
def search_etsy(keyword):
    driver = webdriver.Firefox()
    driver.get("https://www.etsy.com")

    search_bar = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "global-enhancements-search-query"))
    )
    search_bar.click()
    search_bar.send_keys(keyword)
    search_bar.send_keys(Keys.ENTER)

    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "li.wt-list-unstyled"))
    )
    time.sleep(2)

    products = driver.find_elements(By.CSS_SELECTOR, "li.wt-list-unstyled")
    results = []

    for p in products:
        try:
            title_el = p.find_element(By.CSS_SELECTOR, "h3")
            title = title_el.text.strip()

            link_el = p.find_element(By.CSS_SELECTOR, "a.listing-link")
            product_link = link_el.get_attribute("href")

            try:
                store_el = p.find_element(By.CSS_SELECTOR, "p.wt-text-caption a")
                store_name = store_el.text.strip()
                store_link = store_el.get_attribute("href")
            except NoSuchElementException:
                store_name = "N/A"
                store_link = "N/A"

            try:
                feedback_el = p.find_element(By.CSS_SELECTOR, "span.wt-text-body-smaller")
                feedback_text = feedback_el.text.strip().replace("(", "").replace(")", "")
                feedback_count = int(feedback_text) if feedback_text.isdigit() else 0
            except NoSuchElementException:
                feedback_count = 0

            results.append({
                "Title": title,
                "Product Link": product_link,
                "Store Name": store_name,
                "Store Link": store_link,
                "Feedback Count": feedback_count
            })

        except Exception:
            continue

    driver.quit()
    return results


if __name__ == "__main__":
    keyword = input("Enter a keyword to search: ")
    data = search_etsy(keyword)

    if data:
        df = pd.DataFrame(data)
        df.to_csv("etsy_results.csv", index=False)
        print(df.head())
        print(" Saved to etsy_results.csv")
    else:
        print(" No data found.")




# # webdriver = webdriver.current_url("https:://google.com")
# # argv  = sys.argv
# i = 1
# # string = ""
# # if len(argv) == 1:
# #     print("please entry valid search title")
# #     exit()
# # else:
# #     while(i < len(sys.argv)):
# #         string += str(sys.argv[i])
# #         string += " "
# #         i += 
# keyword = input("Enter a keyword to search: ")

# webdriver = webdriver.Firefox()
# webdriver.get("https://etsy.com")

# name = webdriver.title
# print(name)
# search = webdriver.find_element(By.ID, "global-enhancements-search-query")
# search.click()
# time.sleep(1)
# search.send_keys(keyword)
# search.send_keys(Keys.ENTER)
# print(search)
# time.sleep(1)

# try:
#     feedback = WebDriverWait(webdriver, 10).until(
#         EC.presence_of_all_elements_located((By.CLASS_NAME, "wt-text-body-smaller"))
#     )
#     for elem in feedback:
#         text = elem.text.strip()
#         if text:
#             print(text)
# except:
#     print("No feedback found or took too long to load")
# # if feedback:
# #     for i in range(len(feedback)):
# #         number = feedback[i].text.replace("(", "").replace(")", "")
# #         print(number)

#     # print("founded  =", number)
# # except NoSuchElementException:
# #     print("feedback not found")
# # print(feedback.text)                    # Gets: (3.4k)
# # print(feedback.get_attribute("class"))  # Gets: wt-text-body-smaller wt-text-black
# # print(feedback.get_attribute("outerHTML"))  # Gets full HTML tag
# time.sleep(3)

# webdriver.quit()
