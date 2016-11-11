import interlocutor

if __name__ == '__main__':
    file = open("conv.txt", 'w+')
    file.write("ROZMOWA" + "\n")
    intrlocu = interlocutor.Interlocutor()
    conversation = True
    yoursinput = "I live you"#"What do you think about democration"
    list = ["MY name is KK", "Hi", "FREEBSD IS A COMPUTER OPERATING SYSTEM", "ARE YOU AMERICAN", "more than ONE THOUSAND", "ONE THOUSAND", "MY MOTHER DIED", "APPLES IS NOT star", "stop"]
    licznik = 0
    ile = 1

    while(conversation):

        yoursinput = list[licznik] # raw_input("You:  ") #"APPLES IS NOT star"#
        licznik += 1
        print("<<<<< " + yoursinput)

        if yoursinput.__contains__("stop"):# or licznik > ile:
            conversation = False
            break
        try:
            chatt_answer = intrlocu.give_ans(yoursinput)

            file.write("P: " + yoursinput + "\n")
            file.write("C:" + chatt_answer + "\n")
            print(">>> " + chatt_answer)

        except Exception:
            pass


