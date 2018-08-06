from framework.pages.search_page import *
from tests.UI.test_base import TestBase


@pytest.allure.feature('Search')
class TestSearch(TestBase):
    @classmethod
    def setUpClass(cls):
        super(TestSearch, cls).setUpClass()
        cls.search_page = SearchPage(cls.driver)
        cls.search_page.go_to_search_page()

    @pytest.allure.title('Check filtering and sorting')
    def testCheckSearch(self):
        with step('Filter for first registration from 2015'):
            self.search_page.filter_by_first_registration('4')
        with step('Sort cars by Price Descending'):
            self.search_page.sort_by_price_descending()
        with step('Collect information about all cars'):
            self.search_page.collect_information_about_all_cars()
        with step('Verify all cars are filtered by first registration'):
            self.assertTrue(self.search_page.verify_all_cars_filtered_by_first_registration(),
                            'Failed to filter cars by first registration')
        with step("Verify all cars are sorted by price descending"):
            self.assertTrue(self.search_page.verify_cars_ordered_descending(), 'Failed to order cars descending')





