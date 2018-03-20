# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver


class HomePageTests(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super(HomePageTests, cls).setUpClass()
        cls.browser = webdriver.Firefox()
        cls.browser.implicitly_wait(3)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super(HomePageTests, cls).tearDownClass()

    def test_home_page_content(self):
        """Test that the home page renders the task description"""
        self.browser.get(self.live_server_url)
        page_heading = self.browser.find_element_by_tag_name('h1').text
        self.assertEqual('Task Description', page_heading)

        requirements = self.browser.find_elements_by_css_selector('.well ul li')
        self.assertEqual(len(requirements), 3)
        self.assertIn('JavaScript', requirements[0].text)
        self.assertIn('BED file to database', requirements[1].text)
        self.assertIn('description of the regions', requirements[2].text)

    def test_nav_links(self):
        """Test that navigation links to expected pages"""
        self.browser.get(self.live_server_url)

        # Test that the home page links to the BED upload page
        navbar = self.browser.find_element_by_id('navbar')
        navbar_links = navbar.find_elements_by_tag_name('li')
        bed_upload_nav_link = navbar_links[-1]
        self.assertEqual('Upload BED File', bed_upload_nav_link.text)

        bed_upload_nav_link.click()
        page_heading = self.browser.find_element_by_tag_name('h1').text
        self.assertEqual('Upload BED File', page_heading)

        # Test that the BED upload page links to the home page
        navbar = self.browser.find_element_by_id('navbar')
        navbar_links = navbar.find_elements_by_tag_name('li')
        home_nav_link = navbar_links[0]
        self.assertEqual('Home', home_nav_link.text)

        home_nav_link.click()
        page_heading = self.browser.find_element_by_tag_name('h1').text
        self.assertEqual('Task Description', page_heading)
