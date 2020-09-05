#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import binascii
from time import sleep

#перевод строки в биты
def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

#создать сокет и связать с портом
sock = socket.socket()
sock.bind(('', 9090))

#скрытое сообщение, которое хотим отправить
message = "This is a secret message"
#print ("Covert message: " + message)

#переводим в биты
message_bin = text_to_bits(message)

#принять соединение
sock.listen(1)
conn, addr = sock.accept()
print 'connected:', addr

#сообщение для отправки в открытую
msg = "open text"

#отправка этого сообщения по буквам с задержками
print("Sending characters with delays...")
n = 0
count = 0
while(count < len(message_bin)):
    for i in msg:
        conn.send(i.encode())
        if (message_bin[n] == "0"):
            sleep(0.025)
        else:
            sleep(0.1)
        n = (n + 1) % len(message_bin)
        count += 1

#сообщение об окончании   
print ("END")    
conn.send("END")
conn.close()
