

import time
import socket
import threading 
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
port = 12345
s.bind((host,port))
s.listen(5)

clients = []
def Names(msg,exception):
	for client in clients :
		if client != exception :
			client.send(msg)
		
	

def client_no(c):
	while True:
		try:
			message = c.recv(1024).decode()


			if message != "" :
				if message == "QUIT()":
					print(f"Lost the dude:{adrs} ")
					Names(bytes("Lost one soldier :( ", "utf-8"),c)
					for client in clients :
						if client == c :
							clients.remove(c)
							
				
				else :	
					Names(bytes(">>"+ message,"utf-8"),c)
					print("!> ",message)	

		except :	
				break
			

	c.close()	

while True :
	c,adrs = s.accept()
	name = c.recv(1024).decode()
	
	print("connection incoming from : " ,adrs,name)
	Names(bytes(f"{name} has joined the room :D ","utf-8"),c)
	clients.append(c)
	thread = threading.Thread(target=client_no, args=(c,))
	thread.start()
	c.send(bytes(f"welcome on board {name} and if you ever wanna quit press QUIT() and start by pressing ENTER","utf-8"))

