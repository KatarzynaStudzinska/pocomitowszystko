from naoqi import ALProxy

import interlocutor

if __name__ == '__main__':
    # robotIP = "127.0.0.1"
    # PORT = 9559
    # tts = ALProxy("ALTextToSpeech", robotIP, PORT)
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
            # tts.say(chatt_answer)
        except Exception:
            pass