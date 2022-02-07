import pytest
from Page_Object_Model.pages.site.sitemap_xml_page import SitemapXmlPage
from Page_Object_Model.сonfiguration import UrlStartPage


# @pytest.mark.s_r_c
# @pytest.mark.skip
def test_checking_response_statuses_of_all_pages_in_sitemap_xml(browser):  # проверка статутов ответов всех страниц в sitemap.xml
    url_Page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}/sitemap.xml"
    sitemap_xml_page = SitemapXmlPage(browser, url_Page)
    # browser.maximize_window()
    sitemap_xml_page.open(False)
    sitemap_xml_page.checking_response_statuses_of_all_pages_in_sitemap_xml()  # проверка статутов ответов всех страниц в sitemap.xml
