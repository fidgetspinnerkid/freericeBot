from nltk.corpus import wordnet
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
            elif "/" in string:
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
            return int(eval(string))

    @staticmethod
    def similar(w1,w2):
        try:
            w1_syn = [" ".join(i.name().split('_')) for i in wordnet.synsets(w1)[0].lemmas()]
            w2_syn = [" ".join(i.name().split('_')) for i in wordnet.synsets(w2)[0].lemmas()]
            return w1 in w2_syn or w2 in w1_syn
        except:
            return False

    @staticmethod
    def closest_synonyms(word,choices):
        c0,c1,c2,c3 = choices
        syn_list=wordnet.synsets(word)
        for i in syn_list[0].lemmas():
            s=" ".join(i.name().split('_'))
            if Solver.similar(s,c0):
                return c0
            if Solver.similar(s,c1):
                return c1
            if Solver.similar(s,c2):
                return c2
            if Solver.similar(s,c3):
                return c3
            else:
                raise ValueError('Word not found.')
