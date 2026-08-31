from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def add_to_cart(self):
        cartButton = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        cartButton.click()

    def check_cart_price(self):
        productPrice = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_TAG)
        cartPrice = self.browser.find_element(*ProductPageLocators.CART_SUM)

        assert cartPrice.text == productPrice.text, "cart price != product price"

    def check_alert_message(self):
        nameInAlert = self.browser.find_element(*ProductPageLocators.ADDED_TO_CART_PRODUCT).text
        productName = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_TAG).text

        assert nameInAlert==productName, "product name != name in alert"
