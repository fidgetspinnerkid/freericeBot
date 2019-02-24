from selenium import webdriver
from Solver import Solver
from selenium.webdriver.support.ui import WebDriverWait
import selenium
import time

def find_choices(driver):
    element = driver.find_elements_by_class_name("answer-item")
    if element:
        return element
    else:
        return False

def find_question(driver):
    element = driver.find_element_by_xpath("//*[@id=\"question-title\"]/a/b")
    if element:
        return element
    else:
        return False

class Answerer:
    def __init__(self):
        pass

    @staticmethod
    def answer_basic_math(number_of_times):
        driver = webdriver.Firefox()
        driver.get("http://freerice.com/#/basic-math-pre-algebra/16859")
        for i in range(number_of_times):
            time.sleep(0.8)

            assert "Basic Math" in driver.title
            assert "content-area" in driver.page_source
            question = WebDriverWait(driver, 10).until(find_question)

            choices = WebDriverWait(driver, 10).until(find_choices)
            print("DONE WITH WebDriverWait")

            try:
                answer = Solver.solve(question.text)
                print("I KNEW IT!!!!!!!!!!!!!!!!!!!!")
            except selenium.common.exceptions.StaleElementReferenceException:
                choices = WebDriverWait(driver, 4).until(find_choices)
                question = WebDriverWait(driver, 10).until(find_question)
                continue
            except ValueError:
                answer = choices[0].text

            for choice in choices:
                try:
                    if str(answer) == choice.text:
                        choice.click()
                except selenium.common.exceptions.StaleElementReferenceException:
                    choices = driver.find_elements_by_class_name("answer-item")
        driver.close()

    @staticmethod
    def answer_english(number_of_times):
        time.sleep(3)
        driver = webdriver.Firefox()

        driver.get("http://freerice.com/#/english-vocabulary/13442")
        for i in range(number_of_times):

            time.sleep(0.5)

            assert "English" in driver.title
            assert "content-area" in driver.page_source
            question = WebDriverWait(driver, 10).until(find_question)

            choices = WebDriverWait(driver, 10).until(find_choices)
            print("DONE WITH WebDriverWait")

            try:
                answer = Solver.closest_synonyms(question.text, [c.text for c in choices])
                print("I KNEW IT!!!!!!!!!!!!!!!!!!!!")
            except selenium.common.exceptions.StaleElementReferenceException:
                choices = WebDriverWait(driver, 4).until(find_choices)
                question = WebDriverWait(driver, 10).until(find_question)
                continue
            except ValueError:
                answer = choices[0].text

            for choice in choices:
                try:
                    if str(answer) == choice.text:
                        choice.click()
                except selenium.common.exceptions.StaleElementReferenceException:
                    choices = driver.find_elements_by_class_name("answer-item")

        driver.close()

    def answer_chem(number_of_times):
        driver = webdriver.Firefox()
        driver.get("http://freerice.com/#/chemical-symbols-full-list/1079")
        for i in range(number_of_times):
            time.sleep(0.8)

            assert "Chemical" in driver.title
            assert "content-area" in driver.page_source
            question = WebDriverWait(driver, 10).until(find_question)

            choices = WebDriverWait(driver, 10).until(find_choices)
            print("DONE WITH WebDriverWait")

            try:
                answer = Solver.find_symbol(question.text, [i.text for i in choices])
                print("I KNEW IT!!!!!!!!!!!!!!!!!!!!")
            except selenium.common.exceptions.StaleElementReferenceException:
                choices = WebDriverWait(driver, 4).until(find_choices)
                question = WebDriverWait(driver, 10).until(find_question)
                continue
            except ValueError:
                answer = choices[0].text

            for choice in choices:
                try:
                    if str(answer) == choice.text:
                        choice.click()
                except selenium.common.exceptions.StaleElementReferenceException:
                    choices = driver.find_elements_by_class_name("answer-item")
        driver.close()

    def answer_capital(number_of_times):
        driver = webdriver.Firefox()
        driver.get("http://freerice.com/#/world-capitals/13632")
        for i in range(number_of_times):
            time.sleep(0.8)

            assert "Capital" in driver.title
            assert "content-area" in driver.page_source

            question = WebDriverWait(driver, 10).until(find_question)

            choices = WebDriverWait(driver, 10).until(find_choices)
            print("DONE WITH WebDriverWait")

            try:
                answer = Solver.find_capital(question.text, [i.text for i in choices])
                print("I KNEW IT!!!!!!!!!!!!!!!!!!!!")
            except selenium.common.exceptions.StaleElementReferenceException:
                choices = WebDriverWait(driver, 4).until(find_choices)
                question = WebDriverWait(driver, 10).until(find_question)
                continue
            except ValueError:
                answer = choices[0].text

            for choice in choices:
                try:
                    if str(answer) == choice.text:
                        choice.click()
                except selenium.common.exceptions.StaleElementReferenceException:
                    choices = driver.find_elements_by_class_name("answer-item")
        driver.close()
