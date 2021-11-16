from seleniumbase import BaseCase

class HomeTest(BaseCase):

    def setUp(self):
        super().setUp()
        print("RUNNING BEFORE EACH TEST ")

        # LOGIN
        self.open("https://practice.automationbro.com/my-account")
        self.add_text("#username", "testuser123")
        self.add_text("#password", "testuser@123")
        self.click("button[name=login]")
        self.assert_text("Log out", ".woocommerce-MyAccount-content")

        # open home page
        self.open("https://practice.automationbro.com")

    def tearDown(self):
        print("RUNNING AFTER EACH TEST")
        # Logout
        self.open("https://practice.automationbro.com/my-account")
        self.click(".woocommerce-MyAccount-content a[href*=logout]")
        self.assert_element_visible("button[name=login]")

        super().tearDown()


    def test_home_page(self):
        # assert page title
        self.assert_title("Practice E-Commerce Site – Automation Bro")

        # assert logo
        self.assert_element(".custom-logo-link")

        #click on get started button and assert the url
        self.click("#get-started")
        get_started_url = self.get_current_url()
        self.assert_equal(get_started_url, "https://practice.automationbro.com/#get-started")

        # get the text of the header and assert the value
        self.assert_text("Think different. Make different.", "h1")

        # exercise: Scroll to the bottom and assert the copyright text
        self.assert_text("Copyright © 2020 Automation Bro", ".tg-site-footer-section-1")

    def test_menu_links(self):
        expected_links = ['Home', 'About', 'Shop', 'Blog', 'Contact', 'My account', 'Home', 'About', 'Blog', 'Contact', 'Support Form']

        # find menu links elements
        menu_links_el = self.find_elements("li[id*=menu-item]")

        # loop through our menu links
        for idx, link_el in enumerate(menu_links_el):
            #print(idx, link_el.text)
            self.assertEqual(expected_links[idx], link_el.text)

