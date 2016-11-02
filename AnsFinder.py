import interlocutor

if __name__ == '__main__':
    file = open("conv.txt", 'w+')
    intrlocu = interlocutor.Interlocutor()
    conversation = True
    while(conversation):
        yoursinput = raw_input("You:  ")
        if yoursinput.__contains__("stop"):
            conversation = False
            break
        try:
            chatt_answer = intrlocu.give_ans(yoursinput)
            file.write("P: " + yoursinput + "\n")
            file.write("C:" + chatt_answer + "\n")
            print(chatt_answer)
        except Exception:
            pass


