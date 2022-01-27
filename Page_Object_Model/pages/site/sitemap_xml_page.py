from Page_Object_Model.pages.base_page import BasePage
import requests
import time
from Page_Object_Model.locators.locators import SitemapPageLocators


class SitemapXmlPage(BasePage):
    def checking_response_statuses_of_all_pages_in_sitemap_xml(self):  # проверка статутов ответов всех страниц в sitemap.xml
        objects = self.browser.find_elements(*SitemapPageLocators.SECTIONS)
        url_list = []
        url_pages = []
        for object1 in objects:
            url_list.append(object1.text)
        for url in url_list:
            if url[-4:] == '.xml':
                url_pages.append(url)
                self.browser.get(url)
                objects2 = self.browser.find_elements(*SitemapPageLocators.SECTIONS)
                for object2 in objects2:
                    url_list.append(object2.text)
            else:
                url_pages.append(url)
        for url_page in url_pages:
            response = requests.head(url_page)
            if response.status_code != 200:
                print(url_page + ' ' + str(response.status_code))
            # else:
            #     print(url_page)
