from socket import *
serverName='220.181.38.148'
serverPort = 12000 
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence=input('Input Lowercase sentence:')
clientSocket.send(sentence.encode())
modifiedSentence=clientSocket.recv(1024)
print('From Server:',modifiedSentence.decode())
clientSocket.close()