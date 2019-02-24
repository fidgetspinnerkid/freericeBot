from fractions import Fraction
from math import sqrt

class Solver:
    def __init__(self):
        pass
    def var(string):
        if "+" in string:
            splitString = string.split("^")
            return "2A^" + splitString[2]
        elif "x" in string:
            splitString = string.split("x")
            expo = int(splitString[0][2]) + int(splitString[1][3])
            return "A^" + str(expo)
        elif "/" in string:
            splitString = string.split("x")
            expo = int(splitString[0][2]) - int(splitString[1][3])
            return "A^" + str(expo)
    def sqRoot(string):
        string = string.split("root")
        return sqrt(int(string[1]))
    def percents(string):
        string = string.split("% of ")
        perc = int(string[0])/100
        return eval(str(perc) + "*" + string[1])
    def solve(string):
        if "A" in string:
            return Solver.var(string)
        elif "square root" in string:
            return Solver.sqRoot(string)
        elif "of" in string:
            return Solver.percents(string)
        elif string.count('/') > 1:
            if "x" in string:
                string = string.replace('x', '*')
                myDeci = eval(string)
                return Fraction(myDeci).limit_denominator()
            elif "**" in string:
                string = string.replace('^', '**')
                myDeci = eval(string)
                return Fraction(myDeci).limit_denominator()
            elif string.count("/") > 2:
                splitFrac = string.split("/")
                ans = "(" + splitFrac[0] + "/" + splitFrac[1] + ")" + "/" + "(" + splitFrac[2] + "/" + splitFrac[3] + ")"
                myDeci = eval(ans)
                return Fraction(myDeci).limit_denominator()
            else:
                myDeci = eval(string)
                return Fraction(myDeci).limit_denominator()
        elif "x" in string:
            string = string.replace('x', '*')
            return int(eval(string))
        elif "^" in string:
            string = string.replace('^', '**')
            return int(eval(string))
        else:
            return eval(string)
