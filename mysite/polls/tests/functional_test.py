from selenium import webdriver
import requests

def get_links(url):
    """Find all links on page at the given url.
       Return a list of all link addresses, as strings.
    """
    browser.get(url)
    elements = browser.find_elements_by_tag_name('a')
    links = [element.get_attribute('href') for element in elements]
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

    browser = webdriver.Chrome(executable_path=r'C:/chromedriver/chromedriver.exe')
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