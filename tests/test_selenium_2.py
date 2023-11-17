from selenium.webdriver.common.by import By


def test_redirected_url(browser, my_text=None):
    if my_text is None:
        my_text = 'Ukranian news'
    box = browser.find_element(By.ID, 'search-input')
    box.send_keys(my_text)
    search_button = browser.find_element(By.CSS_SELECTOR, '.form > input:nth-child(2)')
    search_button.click()
    assert browser.current_url == 'https://www.ukr.net/'
    browser.save_screenshot('test_2.png')
