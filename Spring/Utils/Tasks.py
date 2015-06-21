class Tasks(object):
	def __init__(self, gameSocket):
		self.gameSocket = gameSocket
		
	def AddItem(self, botInstance, itemId):
		self.gameSocket.Send("%xt%s%i#ai%-1%" + itemId + "%", False)
		
	def JoinRoom(self, botInstance, roomId):
		self.gameSocket.Send("%xt%s%j#jr%-1%" + roomId + "%0%0%", False)
		
	def JoinIgloo(self, botInstance, playerId):
		self.gameSocket.Send("%xt%s%j#jp%-1%" + playerId + "%igloo%", False)
		
	def SendMessage(self, botInstance, message):
		self.gameSocket.Send("%xt%s%m#sm%-1%0%" + message + "%", False)
		
	def SendPosition(self, botInstance, X, Y):
		self.gameSocket.Send("%xt%s%u#sp%" + internalId + "%" + str(X) + "%" + str(Y) + "%", False)
		
	def SendEmote(self, botInstance, emoteId):
		self.gameSocket.Send("%xt%s%u#se%" + internalId + "%" + emoteId + "%", False)
