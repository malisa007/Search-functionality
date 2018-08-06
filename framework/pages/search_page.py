import gevent
import re
import pytest
import time
from allure_commons._allure import step
from gevent import thread

from framework.locators import *
from framework.base_page import BasePage


class SearchPage(BasePage):
    def go_to_search_page(self):
        self.open(SearchPageLocators.search_page_url)

    def filter_by_first_registration(self, year):
        self.click(*SearchPageLocators.year_from_button)
        self.select_by_value(year, *SearchPageLocators.year_filter)

    def sort_by_price_descending(self):
        self.select_by_value('2', *SearchPageLocators.sort_dropdown)
        # '2' = sort by price descending

    def collect_information_about_all_cars(self):
        cars_info = []
        for page in range(1, 10):
            page_button = (By.XPATH, SearchPageLocators.pagination_page_locator.format(page))
            self.click(*(By.XPATH, '//h1'))
            for _ in range(10):
                gevent.sleep(0.5)
                self.scroll_page_down()
            self.move_to_element(*page_button)
            self.click(*page_button)
            titles = self.find_elements(*SearchPageLocators.cars_title)
            years = self.find_elements(*SearchPageLocators.years)
            prices = self.find_elements(*SearchPageLocators.price)
            for car in range(len(titles)):
                price = re.findall("\d+\.\d+", prices[car].text)[0] #Deleting unprinted symbols
                cars_info.append({'title': titles[car].text, 'year': int(years[car].text.replace('•\n''', '')),
                                  'price': float(price)})
        return cars_info

    def verify_all_cars_filtered_by_first_registration(self):
        cars_info = self.collect_information_about_all_cars()
        filtered_cars = list(filter(lambda car: car['year'] <= 2015, cars_info))
        return len(filtered_cars) != 0

    def verify_cars_ordered_descending(self):
        i = 0
        cars_info = self.collect_information_about_all_cars()
        # check that each price value is more than previos one
        while i < len(cars_info)-2:
            if cars_info[i]['price'] < cars_info[i+1]['price']:
                return False
        return True









