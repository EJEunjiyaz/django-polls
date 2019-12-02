import requests
from selenium import webdriver
from django.test import TestCase
from django.utils import timezone

# from polls.models import Question, Choice


def get_links(url):
    """Find all links on page at the given url.
       Return a list of all link addresses, as strings.
    """
    browser = webdriver.Chrome('mysite/polls/tests/chromedriver/chromedriver.exe')
    browser.get(url)
    elements = browser.find_elements_by_tag_name('a')
    links = [element.get_attribute('href') for element in elements]
    browser.close()
    return links

def invalid_urls(urllist):
    """Return invalid urls as a list"""

    invalid_url_list = []
    for url in urllist:
        try:
           request = requests.head(url)
        #    if request.status_code == 200:
        #        print('pass')
        except:
            invalid_url_list.append(url)
    return invalid_url_list
        
def main():
    """Method for testing question 1-4"""

    browser = webdriver.Chrome('mysite/polls/tests/chromedriver/chromedriver.exe')
    browser.get('https://cpske.github.io/ISP/')
    elements = browser.find_elements_by_tag_name('a')
    for element in elements:
        print(element.get_attribute('href'))
    
    link = get_links('https://cpske.github.io/ISP/')
    print(f"\nChecking invalid URLs link. Please wait ...")
    invalid_url_list = invalid_urls(link)
    if len(invalid_url_list) == 0:  # Doesn't have invalid url
        print("There is no bad URLs")
    else:
        print("Bad URLs Here")
        print(*invalid_url_list, sep = "\n")
    browser.close()


class PollsTest(TestCase):
    @classmethod
    def setUpClass(cls):
        """This method is run only once, before any tests are run."""
        q1 = Question(question_text='Who is your favorite singer in TWICE?', pub_date=timezone.now())
        q1.save()
        c1 = Choice(question=q1, choice_text='Nayeon')
        c2 = Choice(question=q1, choice_text='Nayeon', votes=2)
        c1.save()
        c2.save()

    def setUp(self):
        """This method is called before every test."""
        self.browser = webdriver.Chrome('mysite/polls/tests/chromedriver/chromedriver.exe')

    # def test_page(self):

main()