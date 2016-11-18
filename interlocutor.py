import glob
import os
import answerfinder# answerfinder_pusty as answerfinder
import xml.sax
import random

class Interlocutor:
    def __init__(self):

        self.that = ""


    def similarity_to_input(self, tab, input):
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
        print(file_list)
        sorted(file_list)
        print(file_list)
        for filename in glob.glob(os.path.join(path, '*.aiml')):
            print(filename)
            parser.parse(open(filename))

            if ansfinder.no_more == True:#False: #len(ansfinder.choosen_ans) > 0:
                break
        #self.print_tab(ansfinder.choosen_ans)
        choosen, srai_choosen = self.similarity_to_input(ansfinder.choosen_ans, ansfinder.input)
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

        ansfinder, no_more, choosen_ans, srai_choosen = self.parse_file(parser, ansfinder, 'source/' + first_letter)
        if no_more == False and srai_choosen == False:
            ansfinder, no_more, choosen_ans, srai_choosen = self.parse_file(parser, ansfinder, 'source/star' )
        elif srai_choosen:
            return self.give_ans(choosen_ans)


        self.that = ansfinder.ans.upper()
        self.think_dict = ansfinder.think_dict
        self.srai_pattern = ansfinder.srai_pattern

        return choosen_ans
