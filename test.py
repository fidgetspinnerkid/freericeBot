from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from Solver import Solver
from Answerer import Answerer
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

def main():

    Answerer.answer_basic_math(9999999999999999999)

if __name__ == "__main__":
    main()
