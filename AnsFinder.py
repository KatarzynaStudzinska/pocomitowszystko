import interlocutor

if __name__ == '__main__':
    file = open("conv.txt", 'w+')
    file.write("ROZMOWA" + "\n")
    intrlocu = interlocutor.Interlocutor()
    conversation = True
    yoursinput = "I live you"#"What do you think about democration"
    list = ["I am very handsome person", "I am a bit shy person" ,"stop"]
    licznik = 0
    ile = 1

    while(conversation):

        yoursinput = list[licznik] #raw_input("You:  ")
        licznik += 1
        print("<<<<< " + yoursinput)

        if yoursinput == "stop":# or licznik > ile:
            conversation = False
            break
        try:
            chatt_answer = intrlocu.give_ans(yoursinput)

            file.write("P: " + yoursinput + "\n")
            file.write("C:" + chatt_answer + "\n")
            print(">>> " + chatt_answer)

        except Exception:
            pass


