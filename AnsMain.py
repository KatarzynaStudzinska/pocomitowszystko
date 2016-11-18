from naoqi import ALProxy

import interlocutor
from socket import *


if __name__ == '__main__':
    file = open("conv.txt", 'w+')
    file.write("ROZMOWA" + "\n")

    HOST = "192.168.210.109"
    PORT = 5000

    chatterbot = interlocutor.Interlocutor()
    robotIP = "127.0.0.1"
    robotPORT = 9559
    tts = ALProxy("ALTextToSpeech", robotIP, robotPORT)

    s = socket(AF_INET, SOCK_STREAM)
    s.bind((HOST, PORT))
    while True:
        s.listen(1) #how many connections can it receive at one time
        conn, addr = s.accept() #accept the connection
        while True:
            data = conn.recv(1024) #how many bytes of data will the server receive
            print "You: " + data
            chat_ans = chatterbot.give_ans(data)
            print(chat_ans)
            tts.say(chat_ans)

            file.write(data)
            file.write(chat_ans)

            if data == '':
                conn.close()
                break





