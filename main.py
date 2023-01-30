# Created by : Amirhosein abdelzade
# my languages :  germany and english
import string
from googletrans import Translator

# my error class
class My_Exeption(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.__mes = message
        
    def __str__(self):
        return f"{self.__mes}"

# our learning part...if we work several times..the program will be faster
English_Learning_Dic = {}
Germany_Learning_Dic = {}

# for control that our text dont have other languages words
def Controller(text):
    C_text = list(text.split(" "))
    for i in text:
        if i not in string.ascii_letters and i not in string.punctuation and i != " ":
            raise My_Exeption(f"{i} it isn't a valid alphabet...please rewrite again your text")
    return text
            
# our english to germany translator
def English_To_Germany():
    # translation part
    def translator(text):
        translator = Translator()
        T_text = translator.translate(text, dest = "de")
        print(f"{text}  -->  {T_text.text}\n-----------\n")
        English_Learning_Dic[text] = T_text.text
    while True:
        text = input("write your english text : ")
        if text == "~":
            return
        
        # our learning part
        if text in English_Learning_Dic.keys():
            print(f"{text}  -->  {English_Learning_Dic[text]}\n-----------\n")
            continue
        
        try:
            translator(Controller(text))
        except My_Exeption as error:
            print(error)
        
# our germany to english translator
def Germany_To_English():
    # translation part
    def translator(text):
        translator = Translator()
        T_text = translator.translate(text, dest = "en")
        print(f"{text}  -->  {T_text.text}\n-----------\n")
        Germany_Learning_Dic[text] = T_text.text
    while True:
        text = input("write your Germany text : ")
        if text == "~":
            return
        
        if text in Germany_Learning_Dic.keys():
            print(f"{text}  -->  {Germany_Learning_Dic[text]}\n-----------\n")
            continue
        
        try:
            translator(Controller(text))
        except My_Exeption as error:
            print(error)

# intro
def openning():
    print("""\t\t\tIn the name of God
            \t    Wellcome to amir translate
        Pleas give me Germany text...i will translate to english
          if you want to change translate language...type (~)\n\n""")


openning()

# place that translation language change with ~
while True:
    Germany_To_English()
    English_To_Germany()
