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
        for i in range(number_of_times):
            time.sleep(1)
            driver.get("http://freerice.com/#/basic-math-pre-algebra/16859")
            assert "Basic Math" in driver.title

            question = driver.find_element_by_xpath("//*[@id=\"question-title\"]/a/b")

            choices = driver.find_elements_by_class_name("answer-item")

            print("question: "+str(question.text))
            print("choices:")

            for choice in choices:
                print(choice.text)

            answer = Solver.detect(question.text)
            print("answer: "+ str(answer))

            for choice in choices:
                if str(answer) == choice.text:
                    choice.click()
                    break
        driver.close()

    @staticmethod
    def answer_english(number_of_times):
        time.sleep(3)
        driver = webdriver.Firefox()

        driver.get("http://freerice.com/#/english-vocabulary/13442")
        for i in range(number_of_times):

            time.sleep(1)

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
