from selenium import webdriver
from Solver import Solver

class Answerer:
    def __init__(self):
        pass

    @staticmethod
    def answer_basic_math(number_of_times):
        driver = webdriver.Firefox()
        for i in range(number_of_times):
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
