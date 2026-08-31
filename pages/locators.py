from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ADDED_TO_CART_PRODUCT = (By.CSS_SELECTOR, ".alert-safe:nth-child(1) strong")
    PRODUCT_NAME_TAG = (By.CSS_SELECTOR, "div h1")
    CART_SUM = (By.CSS_SELECTOR, ".alert-safe:nth-child(3) strong")
    PRODUCT_PRICE_TAG = (By.CSS_SELECTOR, "div.row div.product_main .price_color")
