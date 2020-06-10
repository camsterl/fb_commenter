from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time as t



browser = webdriver.Chrome('Enter Chrome driver webdriver here')


browser.get('https://www.facebook.com/')

signup_elem = browser.find_element_by_id('email')
signup_elem.send_keys('Enter Email Here')

login_elem = browser.find_element_by_id('pass')
login_elem.send_keys('Enter Password Here')

ins = browser.find_elements_by_tag_name('input')
for x in ins:
    if x.get_attribute('value') == 'Log In':
        x.click() # here logged in
        break
#then key here move to mobile version as that doesn't support javascript
browser.get('https://m.facebook.com')
browser.get('https://m.facebook.com')

t.sleep(5)
pl = browser.find_element_by_id('search_jewel')
pl.click()

el = browser.find_element_by_id('main-search-input')

el.send_keys('Enter User Name Here')
el.send_keys(Keys.ENTER)
t.sleep(3)

temp= ''


el = browser.find_element_by_class_name('_uod')

print("test")
el.click()

# CLICK TIMELINE
#browser.get(temp+'?v=timeline')
t.sleep(10)


# find last post (occurance of comment)
as_el = browser.find_elements_by_tag_name('a')
for a in as_el:
    print(a.text)
    if 'omment' in a.text.strip():
        a.click()
        break
t.sleep(10)


# do actual comment
a = 0
while a != 120:
    ins = browser.find_element_by_id('composerInput')
    ins.send_keys('Enter what you want to say here')
    # submit input
    t.sleep(3)
    ins = browser.find_elements_by_tag_name('button')
    for x in ins:
        if 'Post' in x.get_attribute('value'):
            x.click()
            break
    print("test")
    a = a + 1
    t.sleep(8)


