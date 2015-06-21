import socket
import socks

class torSocket(object):
	def __init__(self, IPAddress = "", Port = 0):
		self.torSocket = socks.socksocket()
		self.torSocket.setproxy(socks.PROXY_TYPE_SOCKS5, '127.0.0.1', 9150, True)
		self.torSocket.settimeout(5)
		if(IPAddress != "" and Port != 0):
			self.Connect(IPAddress, Port)
		
	def newIdentity(self):
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.connect(("127.0.0.1", 9151))   
		s.send("AUTHENTICATE \"my_password\"\r\nSIGNAL NEWNYM\r\n")
		response = s.recv(128)
		s.close()
		if(response.startswith("250 OK")):
			return True
		else:
			return False
		
		
	def Connect(self, stringIp, intPort):
		self.torSocket.connect((stringIp, intPort))
		self.torAddress = self.torSocket.getsockname()
		
	def Send(self, stringPacket, shouldRecv = True, delimiter = chr(0)):
		self.torSocket.send(stringPacket + chr(0))
		print '[Sent] > ' + stringPacket
		if(shouldRecv):
			self.Receive(delimiter = delimiter)
			
	def Receive(self, maxBuffer = 2000, delimiter = chr(0)):
		stringReceived = ''
		listReceive = []
		
		while(stringReceived.endswith(delimiter) == False):
			stringReceived += self.torSocket.recv(maxBuffer)
			
		splitRecieved = stringReceived.split(chr(0))
		
		for receivePacket in splitRecieved:
			if(len(receivePacket) > 1):
				#print '[Receive] > ' + receivePacket
				listReceive.append(receivePacket)
				
		return listReceive