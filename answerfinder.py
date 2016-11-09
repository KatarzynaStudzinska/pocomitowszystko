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
        self.isContext = False
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
        if name == "person" and self.isContext: #or name == "person"
            self.isStar = True
        # if name == "person" and self.isContext: #or name == "person"
        #     self.isStar = True
        if name == "that" and self.isContext:
            self.isThat = True

    def endElement(self, name):

        if name == "think":
            if self.isContext:
                self.isThink = False

        if name == "template":
            self.isTemplate = False
            self.isContext = False
            self.choosen_ans.append([self.pattern])
            self.choosen_ans[-1].append(self.ans)


                # self.no_more = True
        if name == "random" and self.isContext:
            self.isRandom = False
            self.ans = self.ans + random.choice(self.random_table)


        if name == "person":
            self.isPerson = False
        if name == "that":
            self.isThat = False

        if name == "category" and self.isStar == False:
            if self.ans != "":
                self.no_more = True
                self.choosen_ans.append([self.pattern])
                self.choosen_ans[-1].append(self.ans)
                self.pattern = ""
                self.ans = ""

            #self.ans = ""
            self.isContext = False
            self.isTemplate = False
            self.isThatscorrect = False


            self.isThat = False
            self.random_table = []

        # elif name == "template":
        #     self.isTemplate = False


        elif name == "set":
            self.isSet = False


        elif name == "pattern":
            self.isPattern = False
            self.isThat = False
        elif name == "aiml":

            print(str(self.isSrai) + str(self.no_more)+ str(self.isStar))
            pass
        pass

    def characters(self, data):
        if not data.isspace() and not self.isThink:# and re.search('[a-zA-Z]', data): # and not self.no_more: #chyba tak
            

            if self.isSrai and self.ans == "":
                self.srai_pattern = data
                # self.ans = data

            if self.isSet:
                self.ans += data #wydaje mi sie ze tak trzeba :<
                self.think_dict.update({self.think_matter: data})

            if self.isStar:
                self.ans = self.ans + self.star
                self.isStar = False

            if self.isThat:

                # if data != self.that:
                if not self.compare(normalizeText(data), normalizeText(self.that)):
                    self.isContext = False


            if self.isRandom:
                self.random_table.append(data)

            if self.isTemplate and not self.isRandom:

                if self.isThink:
                    pass
                elif self.isThat:
                    if self.isThatscorrect:
                        self.ans += data
                        self.isTemplate = False
                else:
                    self.ans += data
                    # self.isTemplate = False

            if self.isPattern and not self.isThink:
                self.isStar = False
                self.ans = ""
                if data == self.input:

                    self.isContext = True
                    self.pattern = data
                    #self.choosen_ans.append([data])

                # KATARZYNA dodaj tutaj jak jest to samo z gwiazdka
                elif data.__contains__("*"):# and self.input.__contains__(''.join([c for c in data if c not in ('_', '*')])):

                    #if self.compare(data, self.input):
                    if self.compare(data, self.input):
                        #print("compare " + data +self.input)

                        self.star = self.take_star(data, self.input)
                        self.isContext = True
                        self.pattern = data
                if self.isContext:
                    print("context " + data )
                    self.no_more = True

                        #self.choosen_ans.append([data])

    def compare(self, star, text):
        if text == "":
            return False
        if len(star) > len(text):
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



    def compareX(self, star, text):
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
