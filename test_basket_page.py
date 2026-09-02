import pytest
from .pages.basket_page import BasketPage

def  test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = BasketPage(browser, "http://selenium1py.pythonanywhere.com/ru/")
    page.open()
    page.go_to_basket_page_from_header()
    page.check_no_basket_items()
    page.check_empty_basket_notif()
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = BasketPage(browser, "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/")
    page.open()
    page.go_to_basket_page_from_header()
    page.check_no_basket_items()
    page.check_empty_basket_notif()
