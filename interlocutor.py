import glob
import os
import answerfinder
import xml.sax
import random

class Interlocutor:
    def __init__(self):
        self.think_dict = {}
        self.that = ""
        self.srai_pattern = {"name":"Nao", "religion":"Roman Catholic", "master":"Thomas Aquinas", "botmaster":"botmaster",
                             "species": "nao robot"}


    def parse_file(self, parser, ansfinder, path):
        for filename in glob.glob(os.path.join(path, '*.aiml')):
            parser.parse(open(filename))
            if ansfinder.ans != "":
                # print(filename)
                break
        return ansfinder


    def give_ans(self, text_in):
        parser = xml.sax.make_parser()
        text_in = ((''.join([c for c in text_in if c not in (',', '.', '?', '!')]))).upper()
        ansfinder = answerfinder.AnsFinder(text_in, self.that,self.srai_pattern ,self.think_dict )
        parser.setContentHandler(ansfinder)
        # parser.parse("aiml-dir\hello.aiml")

        path_try_conv = 'aiml-dir/try_conv'
        path_conv_keep = 'aiml-dir/keeping_conv'

        ansfinder = self.parse_file(parser, ansfinder, path_try_conv)
        if ansfinder.ans == "":
            ansfinder = self.parse_file(parser, ansfinder, path_conv_keep)
        if ansfinder.isSrai:
            return self.give_ans(ansfinder.ans)
        self.that = ansfinder.ans.upper()
        self.think_dict = ansfinder.think_dict
        self.srai_pattern = ansfinder.srai_pattern
        answer = ansfinder.ans

        # if random.random() > 0.8:
        #     ansfinder = answerfinder.AnsFinder("*", self.that, self.srai_pattern, self.think_dict )
        #     parser.setContentHandler(ansfinder)
        #     additional_ans = self.parse_file(parser, ansfinder, path_conv_keep)
        #     self.that =  additional_ans.ans
        #     answer += " " + additional_ans.ans
        return answer
