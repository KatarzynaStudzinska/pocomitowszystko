import glob
import os
import answerfinder# answerfinder_pusty as answerfinder
import xml.sax
import random

class Interlocutor:
    def __init__(self):
        self.file_dict = {"A":["A0.aiml", "A1.aiml"] ,"B":["B0.aiml"] , "C":["C0.aiml"], "D":["D0.aiml", "D1.aiml", "D2.aiml", "D3.aiml"],
                          "E":["E0.aiml"], "F":["F0.aiml"], "G":["G0.aiml"], "H":["H0.aiml"], "I":["I1.aiml", "I2.aiml", "I3.aiml", "I4.aiml", "I5.aiml", "I6.aiml", "I7.aiml"],
                           "J":["J0.aiml"], "K":["K0.aiml"],"L":["L0.aiml"], "M":["M0.aiml"], "N":["N0.aiml"], "O":["O0.aiml"], "P":["P0.aiml"],
                          "Q":["Q0.aiml"], "R":["R0.aiml"], "S":["S0.aiml"], "T":["T0.aiml"], "U":["U0.aiml"], "V":["V0.aiml"], "W":["W0.aiml", "W1.aiml", "W2.aiml"],
                          "X":["X0.aiml"], "Y":["Y0.aiml"], "Z":["Z0.aiml"], "*":["star4.aiml", "star0.aiml", "star2.aiml", "star1.aiml"]}
        self.that = ""


    def similarity_to_input(self, tab, input):
        print("hello")
        if len(tab) == 0:
            return "", False
        tab_len = []
        for ans in tab:
            if len(input) == len(ans[0]):
                return ans[1], ans[2]
            else:
                tab_len.append(abs(len(ans[0]) - len(input)))

        if tab_len == []:
            return ""
        index = tab_len.index(min(tab_len))
        return tab[index][1], tab[index][2]

    def print_tab(self, tab):
        for line in tab:
            print("nowa linia")
            for elem in line:
                print(elem)

    def parse_file(self, parser, ansfinder, path):
        possible_answer = []
        file_list = glob.glob(os.path.join(path, '*.aiml'))

        for filename in glob.glob(os.path.join(path, '*.aiml')):
            print(filename)
            parser.parse(open(filename))
            print("hello")
            if ansfinder.no_more == True:#False: #len(ansfinder.choosen_ans) > 0:
                break
        #self.print_tab(ansfinder.choosen_ans)

        choosen, srai_choosen = self.similarity_to_input(ansfinder.choosen_ans, ansfinder.input)
        #self.print_tab(ansfinder.choosen_ans)
        return [ansfinder, ansfinder.no_more, choosen, srai_choosen]

    def find_first_letter(self, text_in):
        if text_in[0].isalnum():
            first_letter = text_in[0]
        else:
            if text_in[1].isalnum():
                first_letter = text_in[1]
            else:
                first_letter = "star"
        return first_letter

    def give_ans(self, text_in):
        parser = xml.sax.make_parser()
        text_in = ((''.join([c for c in text_in if c not in (',', '.', '?', '!')]))).upper()
        ansfinder = answerfinder.AnsFinder(text_in, self.that)
        parser.setContentHandler(ansfinder)

        first_letter = self.find_first_letter(text_in)
        print(self.file_dict.get(first_letter))

        ansfinder, no_more, choosen_ans, srai_choosen = self.parse_file(parser, ansfinder, 'source/' + first_letter)
        if no_more == False and srai_choosen == False:
            ansfinder, no_more, choosen_ans, srai_choosen = self.parse_file(parser, ansfinder, 'source/star' )
        elif srai_choosen:
            return self.give_ans(choosen_ans)


        self.that = ansfinder.ans.upper()
        self.think_dict = ansfinder.think_dict
        self.srai_pattern = ansfinder.srai_pattern

        return choosen_ans
