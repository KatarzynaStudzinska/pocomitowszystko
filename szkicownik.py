def comparee( star, text):
    t = 0
    s = 0
    podobne = True

    if len(star) > len(text):
        return False

    if star == "" or text == "":
        return False

    while podobne:
        print(text[t] + star[s])
        t = t + 1
        s = s + 1
        if t == len(text) or s == len(star):
            return True
        if star[s] == "*" and s == len(star) - 1:
            return True
        elif star[s] == "*":
            print("dd")
            s = s + 2
            while not(t == len(text)):
                print(text[t], star[s])
                if t == len(text):
                    return False
                t += 1
                if text[t] == star[s]:
                    break



        if star[s] != text[t]:
            return False
    pass

def compare(star, text):
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


star = '* NOONE'#"HI * TURING TEST"
text = "HI EVERY KK NOONE"

print(str(compare(star, text)))