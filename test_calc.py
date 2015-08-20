import requests
import unittest
import json
import HTMLTestRunner
from   selenium import webdriver
from   selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

class TestCalulator(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        
    def tearDown(self):
        self.browser.close()
        
    def test_additionOfTwoNumbers(self):
        """Function to test Addition operation by API call """
        r = requests.get('https://www.calcatraz.com/calculator/api?c=3%2B3')
        expected_output = 6
        execute_output = r.json()
        self.assertEqual(expected_output, execute_output)
    
    def test_SignUp(self):
        """Function to test SignUp Page """
        browser = self.browser
        browser.get( 'https://www.calcatraz.com/accounts/register/' )
        execute_output = False
        expected_output = True
        # Fetch username, password input boxes and submit button
        username = browser.find_element_by_id( "u" )
        password = browser.find_element_by_name( "p" )
        submit   = browser.find_element_by_id( "loginbtn"   )
         
        # Input text in username and password inputboxes
        username.send_keys( "me"         )
        password.send_keys( "mypass" )
         
        # Click on the submit button
        submit.click()
         
        # Create wait obj with a 5 sec timeout, and default 0.5 poll frequency
        wait = WebDriverWait( browser, 5 )
        
        # test if the page  after sign up  "Enter your name" element
        if browser.find_element_by_name( "n" ) != None:
            execute_output = True
        self.assertEqual(expected_output,execute_output)
        
    def test_loginPage(self):
        """Function to test Login page """
        browser = self.browser
        browser.get( 'https://www.calcatraz.com/accounts/login/' )
        correct_page = 'https://www.calcatraz.com/accounts/login/'
        # Fetch username, password input boxes and submit button
        username = browser.find_element_by_id( "u" )
        password = browser.find_element_by_name( "p" )
        submit   = browser.find_element_by_id( "loginbtn"   )
         
        # Input text in username and password inputboxes
        username.send_keys( "me"         )
        password.send_keys( "mypass" )
         
        # Click on the submit button
        submit.click()
         
        # Create wait obj with a 5 sec timeout, and default 0.5 poll frequency
        wait = WebDriverWait( browser, 5 )
         
        self.assertEqual(browser.current_url,correct_page)
    
    def test_BlogPage(self):
        """Function to test Blog page"""
        actual_blog_url = "http://blog.calcatraz.com/"
        browser = self.browser
        browser.get("https://www.calcatraz.com/calculator/")
        execute_output = False
        expected_output = True
        link = browser.find_element_by_link_text('Blog')
        link.click()
        # Create wait obj with a 5 sec timeout, and default 0.5 poll frequency
        wait = WebDriverWait( browser, 5 )
        print browser.current_url
        self.assertEqual(browser.current_url,actual_blog_url)
        
    def test_QA(self):
        """Function to test Q&A page """
        expected_output = "u'= sin 90\\n= 0.894 radians'"
        browser = self.browser
        browser.get("https://www.calcatraz.com/calculator/")
        enter_question = browser.find_element_by_id( "calcbox" )
        submit   = browser.find_element_by_id( "calcsubmit")
        
        enter_question.send_keys("What is sin90")
        submit.click()
        wait = WebDriverWait( browser, 10 )
        
        answer = browser.find_element_by_class_name("ans")
        execute_output = repr(answer.text)
        self.assertEqual(expected_output,execute_output)
    
    def test_RSSFeed(self):
        """Function to test RSS feed link """
        actual_blog_url = "http://blog.calcatraz.com/category/featured/feed"
        browser = self.browser
        browser.get("https://www.calcatraz.com/calculator/")
        link = browser.find_element_by_id('rss')
        link.click()
        # Create wait obj with a 5 sec timeout, and default 0.5 poll frequency
        wait = WebDriverWait( browser, 5 )
        print browser.current_url
        self.assertEqual(browser.current_url,actual_blog_url)
        
    def test_FollowTwitter(self):
        actual_followTwitter_url = "https://twitter.com/intent/follow?original_referer=https%3A%2F%2Fwww.calcatraz.com%2Fcalculator%2F&ref_src=twsrc%5Etfw&screen_name=calcatrazhq&tw_p=followbutton"
        browser = self.browser
        browser.get("https://www.calcatraz.com/calculator/")
        browser.switch_to.frame(browser.find_element_by_tag_name("iframe"))
        link = browser.find_element_by_id("follow-button")
        Currentwindow = browser.window_handles
        link.click()
        wait = WebDriverWait( browser, 5 )
        newwindow = browser.window_handles
        newwindow = list(set(newwindow) - set(Currentwindow))[0]
        browser.switch_to_window(newwindow)
        # Create wait obj with a 5 sec timeout, and default 0.5 poll frequency
        
        print browser.current_url
        self.assertEqual(browser.current_url,actual_followTwitter_url)
        
suite = unittest.TestLoader().loadTestsFromTestCase(TestCalulator)
unittest.TextTestRunner(verbosity=2).run(suite)

outfile = open(r"C:\Users\enisbak\Desktop\Report.html", "w")
runner = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title='Test Report',
                description='This demonstrates the report output by Nishant Bakshi.'
                )

runner.run(suite)

if __name__ == '__main__': 
    unittest.main()
