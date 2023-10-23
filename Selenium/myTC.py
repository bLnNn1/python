import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from locators import *

global link
link = "https://www.emag.ro/laptop-allview-cu-procesor-intelr-celerontm-j4125-pana-la-2-70-ghz-15-6-full-hd-8gb-256gb-ssd-intelr-uhd-graphics-600-ubuntu-grey-allbook-j/pd/DKJSNDMBM/"

def TC1():
    global tc1_passed
    try:
        global driver
        driver = webdriver.Chrome()

        driver.get(link)
        # Save the product name
        global product_name
        product_name = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, product_name_locator))).text
        # Add product to cart
        addToCart = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, addToCart_locator)))
        addToCart.click()

        # time.sleep(20)

        # Press X button
        xButton = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, xButton_locator)))

        xButton.click()

        # time.sleep(2)

        # Press cart button
        cartButton = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, cartButton_locator)))
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.HOME)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(cartButton))
        cartButton.click()

        # time.sleep(2)

        # Check if the product is in cart
        global cart_product
        cart_product = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, cart_product_locator))).text

        if product_name != cart_product:
            tc1_passed = False
        else:
            tc1_passed = True
    except NoSuchElementException:
        tc1_passed = False

    # time.sleep(2)

def TC2():
    global tc2_passed
    TC1()
    try:
        if tc1_passed is True:
            # Press "Delete" button
            # delete_button = driver.find_element(By.XPATH, "//div[@class='line-item line-item-footer visible-xs visible-sm']//button[@class='btn btn-link btn-remove-product gtm_rp080219 remove-product'][normalize-space()='Sterge']")
            delete_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, delete_button_locator)))

            delete_button.click()

            # time.sleep(2)

            # Press cart button
            # cartButton = driver.find_element(By.ID, "my_cart")
            cartButton = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, cartButton_locator)))
            driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.HOME)

            # WebDriverWait(driver, 10).until(EC.element_to_be_clickable(cartButton))
            cartButton.click()

            # time.sleep(2)

            try:
                cart_product = driver.find_element(By.CLASS_NAME, cart_product_locator)
                tc2_passed = False
            except NoSuchElementException:
                tc2_passed = True

            # time.sleep(5)
        else:
            tc2_passed = False
    except NoSuchElementException:
        tc2_passed = False

def TC3():
    global tc3_passed

    TC1()
    if tc1_passed is True:
        try:
            driver.get(link)

            # Add product to cart
            # addToCart = driver.find_element(By.XPATH, "//button[contains(text(),'Adauga in Cos')]")
            addToCart = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, addToCart_locator_TC3)))
            # WebDriverWait(driver, 10).until(EC.element_to_be_clickable(addToCart))
            addToCart.click()

            # time.sleep(2)

            # Press X button
            # xButton = driver.find_element(By.CSS_SELECTOR, ".em.em-close.gtm_6046yfqs")
            xButton = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, xButton_locator)))
            # WebDriverWait(driver, 10).until(EC.element_to_be_clickable(xButton))
            xButton.click()

            # time.sleep(2)

            # Press cart button
            # cartButton = driver.find_element(By.ID, "my_cart")
            cartButton = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, cartButton_locator)))
            driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.HOME)
            # WebDriverWait(driver, 10).until(EC.element_to_be_clickable(cartButton))
            cartButton.click()

            # time.sleep(7)

            # Check if quantity value has been changed
            qty_value = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, qty_value_locator))).text
            # qty_value = driver.find_element(By.CLASS_NAME, "qty-value").text
            if qty_value != 1:
                tc3_passed = True
            else:
                tc3_passed = False
        except NoSuchElementException:
            tc3_passed = False
    else:
        tc3_passed = False

def TC4():
    global tc4_passed
    TC1()

    if tc1_passed is True:
        try:
            # Press "+" button
            global plus_button
            plus_button = driver.find_element(By.CLASS_NAME, plus_button_locator)
            plus_button.click()

            # Check if quantity value has been changed to 2
            global qty_value
            qty_value = driver.find_element(By.CLASS_NAME, qty_value_locator).text

            if qty_value == "2":
                tc4_passed = True
            else:
                tc4_passed = False
        except NoSuchElementException:
            tc4_passed = False

        # time.sleep(5)

def TC5():
    global tc5_passed

    TC1()

    if tc1_passed is True:
        try:
            # minus_button = driver.find_element(By.CLASS_NAME, "btn.btn-qty.qty-minus")
            minus_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, minus_button_locator)))
            minus_button.click()
        except:
            # Press "+" button
            # plus_button = driver.find_element(By.CLASS_NAME, "btn.btn-qty.qty-plus")
            plus_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, plus_button_locator)))
            plus_button.click()

        # time.sleep(1)

        try:
            time.sleep(2)
            # minus_button = driver.find_element(By.CLASS_NAME, "btn.btn-qty.qty-minus")
            minus_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, minus_button_locator)))
            minus_button.click()

            # time.sleep(2)

            # Check if quantity value has been changed to 1
            # qty_value = driver.find_element(By.CLASS_NAME, "qty-value").text
            qty_value = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, qty_value_locator))).text
            if qty_value == "1":
                tc5_passed = True
            else:
                tc5_passed = False
        except:
            tc5_passed = False

    else:
        tc5_passed = False

def TC6():
    global tc6_passed
    TC1()

    if tc1_passed is True:
        try:
            # Press "Add to favorite" button
            # favorite_button = driver.find_element(By.CLASS_NAME, "remove-product.save-for-later-product.btn-save-for-later-product.gtm_mg160119539")
            favorite_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, favorite_button_locator)))
            favorite_button.click()
            time.sleep(2)

            try:
                # Check the cart
                check_cart = driver.find_element(By.CLASS_NAME, cart_product_locator).text
                # check_cart = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "line-item-title.main-product-title"))).text
                tc6_passed = False
            except:
                # Click heart icon and go to favorite list
                # favorite_list = driver.find_element(By.CLASS_NAME, "em.em-heart.navbar-icon")
                favorite_list = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, favorite_list_locator)))
                favorite_list.click()
                # time.sleep(2)

                # Check if the product is in favorite list
                # favorite_title = driver.find_element(By.CLASS_NAME, "product-title.font-semi-bold.js-product-url ").text
                favorite_title = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, favorite_title_locator))).text
                if product_name == favorite_title:
                    tc6_passed = True
                else:
                    tc6_passed = False
        except:
            tc6_passed = False
    else:
        tc6_passed = False

def TC7():
    global tc7_passed

    TC1()

    if tc1_passed is True:
        try:
            # input_promo = driver.find_element(By.CLASS_NAME, "form-control.js-voucher-code")
            input_promo = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, input_promo_locator)))
            input_promo.send_keys("PROMO_CODE")

            # time.sleep(7)
            # continue_button = driver.find_element(By.XPATH, "//a[@class=' btn btn-emag btn-secondary font-size-md btn-block btn-lg gtm_sn11312018']")
            continue_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, continue_button_locator)))
            continue_button.click()
            tc7_passed = True
        except:
            tc7_passed = False
    else:
        tc7_passed = False


def TCs():
    try:
        if tc1_passed is True:
            print("TC1 - Pass")
        else:
            print("TC1 - Failed")
    except:
        print("TC1 - not runned")

    try:
        if tc2_passed is True:
            print("TC2 - Pass")
        else:
            print("TC2 - Failed")
    except:
        print("TC2 - not runned")

    try:
        if tc3_passed is True:
            print("TC3 - Pass")
        else:
            print("TC3 - Failed")
    except:
        print("TC3 - not runned")

    try:
        if tc4_passed is True:
            print("TC4 - Pass")
        else:
            print("TC4 - Failed")
    except:
        print("TC4 - not runned")

    try:
        if tc5_passed is True:
            print("TC5 - Pass")
        else:
            print("TC5 - Failed")
    except:
        print("TC5 - not runned")

    try:
        if tc6_passed is True:
            print("TC6 - Pass")
        else:
            print("TC6 - Failed")
    except:
        print("TC6 - not runned")

    try:
        if tc7_passed is True:
            print("TC7 - Pass")
        else:
            print("TC7 - Failed")
    except:
        print("TC7 - not runned")

    try:
        if tc8_passed is True:
            print("TC8 - Pass")
        else:
            print("TC8 - Failed")
    except:
        print("TC8 - not runned")

TC1()
TC2()
TC3()
TC4()
TC5()
TC6()
TC7()
TCs()