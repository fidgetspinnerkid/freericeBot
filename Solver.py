class Solver:
    def __init__(self):
        pass

    @staticmethod
    def add(string):
        numbers = string.replace(" ","")
        myList = numbers.split('+')
        firstNum = int(myList[0])
        secondNum = int(myList[1])
        return firstNum + secondNum
        
    @staticmethod
    def mult(string):
        numbers = string.replace(" ","")
        myList = numbers.split('x')
        firstNum = int(myList[0])
        secondNum = int(myList[1])
        return firstNum * secondNum

    @staticmethod
    def detect(string):
        if "+" in string:
            return Solver.add(string)
        else:
            return Solver.mult(string)
