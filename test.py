from selenium import webdriver
from Solver import Solver
from Answerer import Answerer

def main():
    # mySolver = Solver()
    #
    # driver = webdriver.Firefox()
    # driver.get("http://freerice.com/#/basic-math-pre-algebra/16859")
    # assert "Basic Math" in driver.title
    #
    # question = driver.find_element_by_xpath("//*[@id=\"question-title\"]/a/b")
    #
    # choices = driver.find_elements_by_class_name("answer-item")
    #
    # print("question: "+str(question.text))
    # print("choices:")
    #
    # for choice in choices:
    #     print(choice.text)
    #
    # answer = mySolver.detect(question.text)
    # print("answer: "+ str(answer))
    #
    # for choice in choices:
    #     if str(answer) == choice.text:
    #         choice.click()
    #         break
    #
    # assert "Basic Math" in driver.title
    #
    # question = driver.find_element_by_xpath("//*[@id=\"question-title\"]/a/b")
    #
    # choices = driver.find_elements_by_class_name("answer-item")
    #
    # print("question: "+str(question.text))
    # print("choices:")
    # for choice in choices:
    #     print(choice.text)
    #
    # answer = mySolver.detect(question.text)
    # print("answer: "+ str(answer))
    #
    # driver.close()

    Answerer.answer_basic_math(1000)

if __name__ == "__main__":
    main()
