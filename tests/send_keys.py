from selenium.webdriver.common.by import By


def test_type_in_text_box(browser, my_text=None):
    if my_text is None:
        my_text = 'Some text is there'
    box = browser.find_element(By.ID, 'search-input')
    box.send_keys(my_text)
    text = box.get_attribute('value')
    assert text == 'Some text is there'
    browser.save_screenshot('test_1.png')
