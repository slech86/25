import pytest
from Page_Object_Model.pages.site.sitemap_xml_page import SitemapXmlPage
from Page_Object_Model.configuration import UrlStartPage

# pytest --reruns 1 --html=./reports/report.html tests/test_sitemap_xml.py


@pytest.mark.skip
@pytest.mark.sitemap
def test_checking_response_statuses_of_all_pages_in_sitemap_xml(browser):  # проверка статутов ответов всех страниц в sitemap.xml
    url_page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}/sitemap.xml"
    sitemap_xml_page = SitemapXmlPage(browser, url_page)
    # browser.maximize_window()
    sitemap_xml_page.open(False)
    sitemap_xml_page.checking_response_statuses_of_all_pages_in_sitemap_xml()  # проверка статутов ответов всех страниц в sitemap.xml
