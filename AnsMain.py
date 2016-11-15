from naoqi import ALProxy

import interlocutor
from socket import *

if __name__ == '__main__':
    #host and port connected to phone or computer
    HOST = "192.168.0.13"
    PORT = 5000

    # robotIP = "127.0.0.1"
    # robotPORT = 9559
    # tts = ALProxy("ALTextToSpeech", robotIP, robotPORT)


    file = open("conv.txt", 'w+')
    intrlocu = interlocutor.Interlocutor()
    conversation = True
    while(conversation):
        s = socket(AF_INET, SOCK_STREAM)
        s.bind((HOST, PORT))
        s.listen(1) #how many connections can it receive at one time
        conn, addr = s.accept() #accept the connection
        #print "Connected by: " , addr #print the address of the person connected
        while True:
            data = conn.recv(1024) #how many bytes of data will the server receive
            print "You: ", repr(data), addr
            if data != '':
                yoursinput = data
            if data == '':
                conn.close()
                s.close()
                break

            if yoursinput.__contains__("stop"):
                conversation = False
                break
            try:
                print("OKOK")
                chatt_answer = intrlocu.give_ans(yoursinput)
                file.write("P: " + yoursinput + "\n")
                file.write("C:" + chatt_answer + "\n")
                print(chatt_answer)
                # tts.say(chatt_answer)
            except Exception:
                pass