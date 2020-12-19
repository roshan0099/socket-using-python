
import socket
import threading

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
port = 12345

client.connect((host, port))

name = input("Enter your name : ")
client.send(bytes(name,"utf-8"))

print(client.recv(1024).decode())
def sending(client):
	while True :

		msg = input("")
		if msg == "QUIT()" :
			client.send(bytes(msg,"utf-8"))
			print("Bye !!")
			client.close()
			threadR.join()
			break
		else :	
			client.send(bytes(msg,"utf-8"))
			threadR = threading.Thread(target = recieve)
			threadR.start()
	
	
def recieve():
	while True:
		try :
			text = client.recv(1024).decode()
			print(text)
		except :
			break	


sending(client) 
