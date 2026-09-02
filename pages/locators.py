from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASS_INPUT = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASS2_INPUT = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")
class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ADDED_TO_CART_PRODUCT = (By.CSS_SELECTOR, ".alert-safe:nth-child(1) strong")
    PRODUCT_NAME_TAG = (By.CSS_SELECTOR, "div h1")
    CART_SUM = (By.CSS_SELECTOR, ".alert-safe:nth-child(3) strong")
    PRODUCT_PRICE_TAG = (By.CSS_SELECTOR, "div.row div.product_main .price_color")
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CART_BUTTON = (By.CSS_SELECTOR, ".basket-mini a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
class BasketPageLocators():
    BASKET_PRODUCTS = (By.CSS_SELECTOR, ".basket-items")
    BASKET_EMPTY_TEXT = (By.CSS_SELECTOR, "#content_inner p")