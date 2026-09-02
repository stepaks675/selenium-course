from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def check_no_basket_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_PRODUCTS), "There is something in the basket"

    def check_empty_basket_notif(self):
        assert "Ваша корзина пуста" in self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_TEXT).text, "No basket empty notif"