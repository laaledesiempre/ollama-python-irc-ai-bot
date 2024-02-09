import socket
import ollama

# Section 1
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = '<host name or ip>' # have to be ser before started
PORT = 6669 #port # have to be ser before started
NICK = '<nickname>' # have to be ser before started
USERNAME = '<bot username>' # have to be ser before started
REALNAME = '<bot realname>' # have to be ser before started

print('soc created |', s)

s.connect((HOST, PORT))

print('connected to: ', HOST, PORT)

# Section 2
usernam_cr= (f'USER {USERNAME} 0 * :{REALNAME} \r\n').encode()
s.send(usernam_cr)
nick_cr = ('NICK ' + NICK + '\r\n').encode()
s.send(nick_cr)

# Section 3
pinged= False

while 1:
    data = s.recv(4096).decode('utf-8')
    print(data)
    
    if data.find('PING') != -1:
        s.send(str('PONG ' + data.split(':')[1] + '\r\n').encode())
        if not pinged:
            pinged=True
            s.send('JOIN #OPERATION \r\n'.encode()) #chanel
            s.send('PRIVMSG #OPERATION|pony_bot : hi \r\n'.encode())
            
        print('PONG sent \n')

# Section 4
    if data.find('!bot') != -1:
        print("!bot found")
        message=data.split("!bot")[1].replace("\\r\\n","")
        print(message)

        response= ollama.chat(model="tinydolphin",messages=[{
            "role":"user",
            "content":f"{message}",
        },
        ])
 
        string=response["message"]["content"]
 
        print(string)

        s.send((str('PRIVMSG ' + data.split()[2]) + ' '+string+' \r\n').encode())
s.close()