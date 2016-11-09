from xml.sax.handler import ContentHandler
import xml.sax
import xml.parsers.expat
import os, glob
import re
import xml.sax
import random

tab_temple = []
tab_pattern = ""

class AnsFinder(xml.sax.handler.ContentHandler, xml.sax.handler.ErrorHandler):

    def __init__(self, input_text, that, srai_patern, think_dict):
        print("siemaS")
        self.tab_answer = []
        self.choosen_ans = []
        self.srai_pattern = srai_patern
        self.think_dict = think_dict
        self.isThink = False
        self.no_more = False
        self.that = that
        self.input = input_text
        self.curpath = []
        self.isPattern = False
        self.isPerson = True
        self.isTemplate = False
        self.isContext = True
        self.isRandom = False
        self.isHere = False
        self.isSrai = False
        self.isStar = False
        self.isThat = False
        self.isThatscorrect = False
        self.think_matter = ""
        self.isSet = False
        self.isGet = False
        self.ans = ""
        self.srai_pattern = ""
        self.random_table = []
        self.star = ""
        self.pattern = ""


    def getWords(self, text):
        return re.compile('\w+').findall(text)

    def subtractLists(self, a, b):
        return a if len(b) == 0 else [a[:i] + self.subtractLists(a[i+1:], b[1:])
                                  for i in [a.index(b[0])]][0]

    def take_star(self, star, text):
        print("take_star"+star+ text)
        result =""
        for i in range(len(star)):
            if star[i] == "*":
                k = i
                if i != len(star) - 1:
                    while text[k] != " ":
                        result += (text[k])
                        k += 1
                else:
                    while k < len(text):
                        result += text[k]
                        k += 1
        print("res "+ result)
        return result

    def startElement(self, name, attrs):
        #serve think
        if name == "think" and self.isContext:
            self.isThink = True

        if name == "set" and self.isContext:
            self.isSet = True
            self.think_matter = attrs.get('name', "")

        if (name == "get" or name == "bot") and self.isContext:
            get_name = attrs.get('name', "")
            if get_name in self.think_dict:
                self.ans += self.think_dict[get_name]
            if get_name in self.srai_pattern:
                self.ans += self.srai_pattern[get_name]

        #name
        if name == "pattern":
            self.isPattern = True
        if name == "template" and self.isContext:
            self.isTemplate = True
        if name == "random" and self.isContext:
            self.isRandom = True
        if name == "srai" and self.isContext:
            self.isSrai = True
        if name == "star" and self.isContext: #or name == "person"
            self.isStar = True
        # if name == "person" and self.isContext: #or name == "person"
        #     self.isStar = True
        if name == "that" and self.isContext:
            self.isThat = True

    def endElement(self, name):
        print("end " + name)

        if name == "think":
            self.isThink = False

        if name == "set":
            self.isSet = False

        #name
        if name == "pattern":
            self.isPattern = False
        if name == "template" and self.isContext:
            self.isTemplate = False
        if name == "random" and self.isContext:
            self.isRandom = False
        if name == "srai" and self.isContext:
            self.isSrai = False

        # if name == "person" and self.isContext: #or name == "person"
        #     self.isStar = True
        if name == "that" and self.isContext:
            self.isThat = False
        if name == "category":
            self.isStar == False
        pass

    def characters(self, data):
        if not data.isspace():
            if self.isPattern:
                if data.__contains__("*"):
                    self.star = self.take_star(data, self.input)
                print("pater", data)
            if self.isTemplate:

                print("temple", data)
            if self.isStar:
                print("star", self.star)
            pass
    def compare(self, star, text):
        t = 0
        s = 0
        podobne = True
        if star == "" or text == "":
            return False
        while podobne:
            t = t + 1
            s = s + 1
            if t == len(text) or s == len(star):
                return True
            elif star[s] == "*":
                return True
            elif star[s] != text[t]:
                return False
        pass

def compare(star, text):
    if text == "":
        return False
    t = 0
    s = 0
    podobne = True
    while podobne or s < len(star) - 1:
        if star[s] != "*" and star[s] != text[t]: #jezeli ktory po prostu sie nie zgadza
            return False

        if star[s] == "*":
            if len(star) == s + 1:
                return True
            else:
                literka = star[s+2]
                while t < len(text):
                    if text[t] == star[s+2] and text[t+ 1] == star[s+3] and text[-1] == star[-1]:
                        return True
                    t += 1
                return False
        t += 1
        s += 1

    return True

def normalizeText(text):
    return ((''.join([c for c in text if c not in (',', '.', '?', '!')]))).upper()
