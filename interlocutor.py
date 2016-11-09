import glob
import os
import answerfinder# answerfinder_pusty as answerfinder
import xml.sax
import random

class Interlocutor:
    def __init__(self):
        self.think_dict = {}
        self.that = ""
        self.srai_pattern = {"name":"Nao", "religion":"Roman Catholic", "master":"Thomas Aquinas", "botmaster":"botmaster",
                             "species": "nao robot"}

    def similarity_to_input(self, tab, input):
        tab_len = []
        for ans in tab:
            if len(input) == len(ans[0]):
                return ans[1]
            else:
                tab_len.append(abs(len(ans[0]) - len(input)))

        if tab_len == []:
            return ""
        index = tab_len.index(min(tab_len))
        return tab[index][1]

    def print_tab(self, tab):
        for line in tab:
            print("nowa linia")
            for elem in line:
                print(elem)

    def parse_file(self, parser, ansfinder, path):
        possible_answer = []
        for filename in glob.glob(os.path.join(path, '*.aiml')):
            print(filename + " start")
            parser.parse(open(filename))
            if ansfinder.no_more == True:#False: #len(ansfinder.choosen_ans) > 0:
                break
        choosen = self.similarity_to_input(ansfinder.choosen_ans, ansfinder.input)
        return [ansfinder, ansfinder.no_more, choosen]


    def give_ans(self, text_in):
        parser = xml.sax.make_parser()
        text_in = ((''.join([c for c in text_in if c not in (',', '.', '?', '!')]))).upper()
        ansfinder = answerfinder.AnsFinder(text_in, self.that, self.srai_pattern, self.think_dict)
        parser.setContentHandler(ansfinder)

        #ansfinder = self.parse_file(parser, ansfinder, 'source/star' )
        ansfinder, no_more, choosen_ans = self.parse_file(parser, ansfinder, 'source/' + text_in[0])
        print(choosen_ans + ansfinder.srai_pattern)
        if no_more == False and ansfinder.isSrai == False:

            ansfinder, no_more, choosen_ans = self.parse_file(parser, ansfinder, 'source/star' )
        elif ansfinder.isSrai:
            print(ansfinder)
            print("jestesmy w srai")
            return self.give_ans(choosen_ans)



        # ansfinder = self.parse_file(parser, ansfinder, 'source/' + text_in[0])
        # print(self.similarity_to_input(ansfinder.choosen_ans, ansfinder.input))
        # if ansfinder.ans == "":
        #     ansfinder = self.parse_file(parser, ansfinder, 'source/star')


        self.that = ansfinder.ans.upper()
        self.think_dict = ansfinder.think_dict
        self.srai_pattern = ansfinder.srai_pattern

        return choosen_ans
