# !!!    AUTOMATION TO SEARCH FOR THE LOWEST AND HIGHEST PRICE FROM MULTIPLE WEB PAGES    !!!

import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://www.emag.ro/laptopuri/filter/produse-la-super-pret-f9902,top-favorite-v40/sort-priceasc/c?ref=lst_leftbar_9902_40")

print(driver.title)

# driver.find_element(By.CLASS_NAME, "navbar-aux-content__departments").click()
# time.sleep(3)
# driver.find_element(By.CSS_SELECTOR, ".megamenu-list-department.js-megamenu-list-department[data-id='1']").click()
# time.sleep(2)
# driver.find_element(By.CSS_SELECTOR, ".ph-widget.ph-collapse-one.megamenu-item.megamenu-item-heading.megamenu-item-first-relative[href='/laptopuri-accesorii/sd?ref=hp_menu_quick-nav_1_0&type=subdepartment']").click()
# time.sleep(2)
# driver.find_element(By.CSS_SELECTOR, ".megamenu-item[href='/laptopuri/c?ref=hp_menu_quick-nav_1_1&type=category']").click()
time.sleep(2)


laptop_dict = dict()


flag = 0
while (flag == 0):
    laptop_list = driver.find_element(By.CSS_SELECTOR, "#card_grid")

    laptops = laptop_list.find_elements(By.XPATH, '//div[@data-category-trail="Laptop, Tablete & Telefoane/Laptopuri si accesorii/Laptop / Notebook"]')

    for lap in laptops:
        name = lap.find_element(By.CLASS_NAME, 'card-v2-title-wrapper').text
        price = lap.find_element(By.CLASS_NAME, 'product-new-price').text
        laptop_dict[name] = price

    try:
        button_next_page = driver.find_element(By.CSS_SELECTOR, "a[aria-label='Next']")
        location_next_page = button_next_page.location
        # scroll to next page button
        driver.execute_script(f"window.scrollBy(0,{location_next_page['y'] - 200})", "")
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(button_next_page))

        button_next_page.click()
        time.sleep(2)
    except NoSuchElementException:
        flag = 1
        print("The end.")

print()
print(laptop_dict)
print()

def min_value(dictionar):
    min_value = float('inf')
    min_key = ''

    for key, value in dictionar.items():
        # Eliminate '.', replace ',' with '.' and eliminate ' Lei'
        value_without_lei = float(value.replace('de la','').replace('.', '').replace(',', '.').replace(' Lei', ''))

        # Min formula
        if value_without_lei < min_value:
            min_value = value_without_lei
            min_key = key

    return f'Cel mai ieftin laptop:\n{min_key} la pretul de {min_value} Lei'

def max_value(dictionar):
    max_value = 0
    max_key = ''

    for key, value in dictionar.items():
        # Eliminate '.', replace ',' with '.' and eliminate ' Lei'
        value_without_lei = float(value.replace('de la','').replace('.', '').replace(',', '.').replace(' Lei', ''))

        # Min formula
        if value_without_lei > max_value:
            max_value = value_without_lei
            max_key = key

    return f'Cel mai scump laptop:\n{max_key} la pretul de {max_value} Lei'

print(min_value(laptop_dict))
print(max_value(laptop_dict))

time.sleep(10)
