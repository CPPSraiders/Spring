from Utils.torSocket    import torSocket
from Cryptography.Crypt import Crypt
from Parsers.XMLParser  import XMLParser
from Parsers.XTParser   import XTParser
from time               import sleep
from random             import randrange

class Bot(object):
	def __init__(self, Username, Password, ServerName):
		self.Username   = Username
		self.Password   = Password
		self.ServerName = ServerName
		self.xtParser   = XTParser()
		
	def setSockets(self, loginSocket, gameSocket):
		self.loginSocket = loginSocket
		self.gameSocket  = gameSocket
		
	def doLogin(self):
		try:
			self.loginSocket.Send('<policy-file-request/>')
			self.loginSocket.Send('<msg t=\'sys\'><body action=\'verChk\' r=\'0\'><ver v=\'153\' /></body></msg>')
			self.loginSocket.Send('<msg t=\'sys\'><body action=\'rndK\' r=\'-1\'></body></msg>', False)
			randomKey = XMLParser().getAttribute(self.loginSocket.Receive()[0], "k")
			print '[randomKey] > ' + randomKey
			self.loginSocket.Send('<msg t=\'sys\'><body action=\'login\' r=\'0\'><login z=\'w1\'><nick><![CDATA[' + self.Username + ']]></nick><pword><![CDATA[' + Crypt().getLoginHash(self.Password, randomKey) + ']]></pword></login></body></msg>', False)
			parsedXT = self.xtParser.ParseRaw(self.loginSocket.Receive()[0])
			if(parsedXT[0] == 'l'):
				print self.Username + ' has logged into the server successfully.'
				self.playerString  = parsedXT[10]
				self.playerId  = parsedXT[2]
				self.playerKey = parsedXT[3]
				self.gameHash = self.playerString.split('|')[3] + '#' + parsedXT[11]
				self.doGame()
			elif(parsedXT[0] == 'e'):
				pass # not added error handling yet
		except:
			sleep(5)
			self.loginSocket.newIdentity()
			self.gameSocket.newIdentity()
			self.doLogin()
			
	def doGame(self):
		try:
			self.gameSocket.Send('<policy-file-request/>')
			self.gameSocket.Send('<msg t=\'sys\'><body action=\'verChk\' r=\'0\'><ver v=\'153\' /></body></msg>')
			self.gameSocket.Send('<msg t=\'sys\'><body action=\'rndK\' r=\'-1\'></body></msg>', False)
			randomKey = XMLParser().getAttribute(self.gameSocket.Receive()[0], "k")
			print '[randomKey] > ' + randomKey
			self.gameSocket.Send('<msg t=\'sys\'><body action=\'login\' r=\'0\'><login z=\'w1\'><nick><![CDATA[' + self.playerString + ']]></nick><pword><![CDATA[' + self.gameHash + ']]></pword></login></body></msg>', False)
			parsedXT = self.xtParser.ParseRaw(self.gameSocket.Receive()[0])
			if(parsedXT[0] == 'l'):
				print self.Username + ' has logged into the game successfully.'
				self.gameSocket.Send('%xt%s%j#jr%-1%100%0%0%')
				while 1:
					self.gameSocket.Send('%xt%s%u#sp%' + str(randrange(10, 20))+ '%' + str(randrange(100, 400)) + '%' + str(randrange(100, 400)) + '%', False))
					sleep(0.5)
					self.gameSocket.Send('%xt%s%u#sj%' + str(randrange(10, 20))+ '%' + str(randrange(1, 20)) + '%', False)
					sleep(0.5)
					self.gameSocket.Send('%xt%s%u#sb%' + str(randrange(10, 20))+ '%' + str(randrange(100, 400)) + '%' + str(randrange(100, 400)) + '%', False)
					sleep(0.5)
					self.gameSocket.Send('%xt%s%u#se%' + str(randrange(10, 20))+ '%19%', False) #' + str(randrange(1, 50))+ '
					sleep(0.5)
		except:
			self.loginSocket.newIdentity()
			self.gameSocket.newIdentity()
			self.doLogin()
				
