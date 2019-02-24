from nltk.corpus import wordnet

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
