#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
from sys import stdout
from time import time
import binascii

#перевод битов в символы
def bits_to_text(b):
   return ''.join(chr(int(''.join(x), 2)) for x in zip(*[iter(b)]*8))

  
#создание сокета
sock = socket.socket()
sock.connect(('localhost', 9090))

data = sock.recv(1024).decode()

covert_bin = ""
conert = ""
print("Binary received:")

#принимаем сообщение и считаем задержки между символами
while (data.rstrip("\n") != "END"):
    stdout.flush()
    t0 = time()
    data = sock.recv(1024)
    t1 = time()
    delta = round(t1 - t0, 3)
    
    if (delta >= 0.1):
        covert_bin += "1"
        stdout.write("1")
    else:
        covert_bin += "0"
        stdout.write("0")
      
sock.close()
covert = bits_to_text(covert_bin)
print ("\nMessage resieved: \n" + covert)

print (data)
