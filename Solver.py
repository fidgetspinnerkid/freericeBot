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
    
    #Find best fit word
    from nltk.corpus import wordnet

    def syn_eval_v1(word,c0,c1,c2,c3):
        syn_list=wordnet.synsets(word)
        for i in syn_list[0].lemmas():
            s=" ".join(i.name().split('_'))
            if(s==c0):
                return c0
            if s==c1:
                return c1
            if s==c2:
                return c2
            if s==c3:
                return c3
            else:
                raise ValueError('Word not found.')
    
    #Translate
    
    from googletrans import Translator
    
    def translate_to_en(word):
        tra=Translator()
        return tra.translate("hello").text
