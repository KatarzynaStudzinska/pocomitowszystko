import interlocutor

if __name__ == '__main__':
    file = open("conv.txt", 'w+')
    file.write("ROZMOWA" + "\n")
    intrlocu = interlocutor.Interlocutor()
    conversation = True
    yoursinput = "I live you"#"What do you think about democration"

    licznik = 0
    ile = 1

    while(conversation):

        yoursinput =raw_input("You:  ") #"APPLES IS NOT star"#

        if yoursinput.__contains__("stop"):# or licznik > ile:
            conversation = False
            break
        try:
            chatt_answer = intrlocu.give_ans(yoursinput)

            file.write("P: " + chatt_answer + "\n")
            #file.write("C:" + chatt_answer + "\n")
            print(">>> " + chatt_answer)

        except Exception:
            pass


