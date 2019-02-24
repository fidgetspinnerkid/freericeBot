class Solver:
    def __init__(self):
        pass
    def add(string):
        numbers = string.replace(" ","")
        myList = numbers.split('+')
        firstNum = int(myList[0])
        secondNum = int(myList[1])
        return firstNum + secondNum
    def mult(string):
        numbers = string.replace(" ","")
        myList = numbers.split('x')
        firstNum = int(myList[0])
        secondNum = int(myList[1])
        return firstNum * secondNum
    def detect(string):
        if "+" in string:
            return Solver.add(string)
        else:
            return Solver.mult(string)
