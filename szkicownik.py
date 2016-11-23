def compare(star, text):
        # jezeli mamy jakis syf w funckji
        if star == text:
            return True

        if text == "":
            return False

        # jezeli mamy
        if star.count("*") > 1:
            star_set = star.split(" ")
            print(star_set)
            for word in star_set:

                if not text.__contains__(word) and word != "*":
                    print word
                    return False
            return True



        elif len(star) > len(text):
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

                    while t < len(text):

                        #if text[t] == star[s+2] and text[t + 1] == star[s+3] and text[-1] == star[-1]:
                        if text[t] == star[s+2] and text[-2] == star[-2] and text[-1] == star[-1]:
                            return True
                        t += 1
                    return False
            t += 1
            s += 1

        return True

import re



text1 = "WHAT IS YOUR FAVORITE *"
text2 = "WHAT IS YOUR FAVORITE BOOK"
print(str(compare(text1, text2)))