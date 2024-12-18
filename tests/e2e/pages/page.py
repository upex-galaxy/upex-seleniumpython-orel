from ..utils.locators import Locators
from ..utils.actions import Actions
from ..utils.assertions import Assertions
from ..utils.helpers import Helpers

class Page:
    def __init__(self, driver):
        self.driver = driver
        self.locators = Locators(driver)
        self.actions = Actions(driver)
        self.assertions = Assertions(driver)
        self.helpers = Helpers(driver)

