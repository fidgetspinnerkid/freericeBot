from selenium import webdriver
from Solver import Solver
from selenium.webdriver.support.ui import WebDriverWait
import selenium
import time
import re

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

def find_rice_given(driver):
    element = driver.find_element_by_xpath("//*[@id=\"game-status-right\"]")
    if element:
        return element
    else:
        return False

class Answerer:
    def __init__(self):
        pass

    @staticmethod
    def answer_translate(number_of_times):
        url = "http://freerice.com/#/spanish/16116"
        solve_func = Solver.translate_to_en_v2

        driver = webdriver.Firefox()
        driver.get(url)
        for i in range(number_of_times):
            time.sleep(0.8)
            # if i>2:
            #     rice_sentence = WebDriverWait(driver, 10).until(find_rice_given)
            #     rice_num = int(re.search(r'\d+', rice_sentence.text).group())
            #     print("rice given"+str(rice_num))
            assert "content-area" in driver.page_source

            question = WebDriverWait(driver, 10).until(find_question)

            choices = WebDriverWait(driver, 10).until(find_choices)

            try:
                answer = solve_func(question.text, [i.text for i in choices])
            except selenium.common.exceptions.StaleElementReferenceException:
                choices = WebDriverWait(driver, 4).until(find_choices)
                question = WebDriverWait(driver, 10).until(find_question)
                continue
            # except ValueError:
            #     print("VALUE ERROR")
            #     answer = choices[0].text


            for choice in choices:
                try:
                    if str(answer) in choice.text or choice.text in str(answer):
                        choice.click()
                except selenium.common.exceptions.StaleElementReferenceException:
                    choices = driver.find_elements_by_class_name("answer-item")
    @staticmethod
    def answer_basic_math(number_of_times):
        Answerer.answer(number_of_times, "http://freerice.com/#/basic-math-pre-algebra/17420", Solver.solve)

    @staticmethod
    def answer_mult(number_of_times):
        Answerer.answer(number_of_times, "http://freerice.com/#/multiplication-table/17501", Solver.solve)
    @staticmethod
    def answer_english(number_of_times):

        Answerer.answer(number_of_times, "http://freerice.com/#/english-vocabulary/13442", Solver.closest_synonyms)
    @staticmethod
    def answer_chem(number_of_times):
        Answerer.answer(number_of_times,"http://freerice.com/#/chemical-symbols-full-list/1079", Solver.find_symbol)

    @staticmethod
    def answer_capital(number_of_times):
        Answerer.answer(number_of_times, "http://freerice.com/#/world-capitals/13632", Solver.find_capital)

    @staticmethod
    def answer(number_of_times, url, solve_func):
        driver = webdriver.Firefox()
        driver.get(url)
        for i in range(number_of_times):
            time.sleep(0.8)
            if i>2:
                rice_sentence = WebDriverWait(driver, 10).until(find_rice_given)
                rice_num = int(re.search(r'\d+', rice_sentence.text).group())
                print("rice given"+str(rice_num))
            assert "content-area" in driver.page_source

            question = WebDriverWait(driver, 10).until(find_question)

            choices = WebDriverWait(driver, 10).until(find_choices)

            try:
                answer = solve_func(question.text, [i.text for i in choices])
            except selenium.common.exceptions.StaleElementReferenceException:
                choices = WebDriverWait(driver, 4).until(find_choices)
                question = WebDriverWait(driver, 10).until(find_question)
                continue
            except ValueError:
                answer = choices[0].text

            for choice in choices:
                try:
                    if str(answer) in choice.text or choice.text in str(answer):
                        choice.click()
                except selenium.common.exceptions.StaleElementReferenceException:
                    choices = driver.find_elements_by_class_name("answer-item")

        rice_sentence = WebDriverWait(driver, 10).until(find_rice_given)
        rice_num = int(re.search(r'\d+', rice_sentence).group())
        print("rice given: "+str(rice_num))
        driver.close()
