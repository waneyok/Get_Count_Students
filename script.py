from selenium import webdriver
from selenium.webdriver.common.by import By
#Позитивный тест(Данные валидны)
def test_get_count_students():
    # Подключение браузера и ссылки сайта
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get("https://psxt.ucoz.com/")
    # Поиск и проверка нужных элементов
    try:
        # need_link = browser.find_element(
        #     By.LINK_TEXT, "ИНФОРМАЦИЯ ДЛЯ ПОСТУПАЮЩИХ"
        # )
        # need_link = browser.find_element(By.CSS_SELECTOR, "div.nabor2 p:nth-child(3) a:nth-child(1)")
        need_link = browser.find_element(By.XPATH, "//*[contains(text(), 'Информация')]")
        need_link.click()
        
        # tables = browser.find_elements(By.CSS_SELECTOR, "table.MsoTableGrid")
        tables = browser.find_elements(By.XPATH, "//table[contains(@class, 'MsoTableGrid')]")
        
        # tb_element = tables[1].find_element(
        #     By.CSS_SELECTOR, "tr:nth-child(3) td:nth-child(3)"
        # )
        tb_element = tables[1].find_element(
            By.XPATH, "./tr[3]/td[3]"
        )
        
        # tb_spec_name = tables[1].find_element(
        #     By.CSS_SELECTOR, "tr:nth-child(3) td:nth-child(1)"
        # )
        tb_spec_name = tables[1].find_element(
            By.XPATH, "./tr[3]/td[1]"
        )
        
        print(f"Количество заявлений = {tb_element.text} по специальности '{tb_spec_name.text}'")
    except Exception as e:
        print(f"Произошла ошибка при выполнении теста: {e}")
def test_get_count_negative():
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get("https://psxt.ucoz.com/")
    try:
        need_link = browser.find_element(
            By.LINK_TEXT, "ИНФОРМАЦИЯ ДЛЯ ПОСТУПАЮЩИХ"
        )
        need_link.click()
        tables = browser.find_elements(By.CSS_SELECTOR, "table.MsoTableGrid")
        tb_element = tables[1].find_element(
            By.CSS_SELECTOR, "tr:nth-child(3.0) td:nth-child(13)"
        )
        print(f"Количество заявлений{tb_element.text}")
    except Exception as e:
        print(f"Произошла ошибка при выполнении теста: {e}")
test_get_count_students()
