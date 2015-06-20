from Spring.Bot import Bot
from Spring.Utils.torSocket import torSocket
from threading import Thread
from time import sleep

torDictionary = {}

def connectBot(username, password):
	loginSocket = torSocket('167.114.67.67', 9876)
	gameSocket = torSocket('198.245.53.39', 3724)
	print loginSocket.torAddress
	while(loginSocket.torAddress in torDictionary):
		sleep(5)
		loginSocket.newIdentity()
		gameSocket.newIdentity()
	b = Bot(username, password, 'Server Name')
	torDictionary[loginSocket.torAddress] = b
	b.setSockets(loginSocket, gameSocket)
	b.doLogin()
		
		
	

accounts = open('accounts.txt', 'r').read().splitlines()
for account in accounts:
	accSplit = account.split(":")
	Thread(target=connectBot, args=(accSplit[0], accSplit[1])).start()
	sleep(1)
	#connectBot(accSplit[0], accSplit[1])

while 1:
	raw_input()