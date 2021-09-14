import time

from selenium import webdriver


#Открыть страницу http://google.com/ncr
driver = webdriver.Firefox(executable_path='/Users/user/PycharmProjects/pythonProject/geckodriver')
driver.get('http://google.com/ncr')

#Выполнить поиск слова “selenide”
driver.find_element_by_xpath('//input').send_keys("selenide" + "\n")
driver.find_element_by_xpath('//input').submit()

time.sleep(2)

#Проверить, что первый результат – ссылка на сайт selenide.org.
results = driver.find_elements_by_xpath(".//*[@id='rso']//h3/a")
results[0].click()
time.sleep(2)
print(driver.current_url)
assert 'selenide' in driver.current_url


#Перейти в раздел поиска изображений

driver.back()
time.sleep(2)
driver.find_element_by_link_text('Images').click()


#Проверить, что первое изображение неким образом связано с сайтом selenide.org.

time.sleep(2)
results = driver.find_elements_by_xpath("//div[@jsname='r5xl4']/div[@data-ow='352']/a")
assert 'selenide.org' in results[1].text


#Вернуться в раздел поиска Все

driver.find_element_by_link_text('Все').click()
time.sleep(2)


#Проверить, что первый результат такой же, как и на шаге 3.

results = driver.find_elements_by_xpath(".//*[@id='rso']//h3/a")
results[0].click()
time.sleep(2)

assert 'selenide' in driver.current_url

driver.close()