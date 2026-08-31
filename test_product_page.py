from selenium.webdriver.common.by import By
from .pages.product_page import ProductPage

def test_product_page(browser):
    page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear")
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.check_alert_message()
    page.check_cart_price()
    