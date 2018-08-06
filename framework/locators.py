from selenium.webdriver.common.by import By
from configuration.config_parse import *


class SearchPageLocators:
    search_page_url = "search/"
    cars_title = (By.XPATH, "//div[@data-qa-selector = 'title']")
    years = (By.XPATH, "//li[@data-qa-selector = 'spec'][1]")
    price = (By.XPATH, "//div[@data-qa-selector = 'price']")
    year_from_button = (By.XPATH, "//*[@id='app']/div/main/div[4]/div/div[1]/div/div/div/div[3]/div[1]")
    year_filter = (By.XPATH, "//*[@id='app']/div/main/div[4]/div/div[1]/div/div/div/div[3]/div[2]/div/select")
    sort_dropdown = (By.XPATH, "//*[@id='app']/div/main/div[4]/div/div[2]/div/div[1]/div[3]/div/div/select")
    pagination_page_locator = "//ul[@class = 'pagination']/li[.='{}']/a"
