from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def test_redirected_url(browser_1, my_text=None):
    if my_text is None:
        my_text = 'deepl'
    box = browser_1.find_element(By.ID, 'APjFqb')
    box.send_keys(my_text)
    box.send_keys(Keys.RETURN)
    result_element = browser_1.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a/h3')
    result_text = result_element.text
    assert result_text == 'Самый точный переводчик в мире - DeepL Translate'
    browser_1.save_screenshot('test_3.png')
