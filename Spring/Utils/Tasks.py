class Tasks(object):
	def __init__(self, gameSocket):
		self.gameSocket = gameSocket
		
	def AddItem(self, itemId):
		self.gameSocket.Send('%xt%s%i#ai%-1%' + str(itemId) + '%', False) #
		
	def JoinRoom(self, roomId):
		self.gameSocket.Send('%xt%s%j#jr%-1%' + str(roomId) + '%0%0%', False)
		
	def JoinIgloo(self, playerId):
		self.gameSocket.Send('%xt%s%j#jp%-1%' + str(playerId) + '%igloo%', False)
		
	def SendMessage(self, message):
		self.gameSocket.Send('%xt%s%m#sm%-1%0%' + str(message) + '%', False)
		
	def SendPosition(self, X, Y):
		self.gameSocket.Send('%xt%s%u#sp%-1%' + str(X) + '%' + str(Y) + '%', False)
		
	def SendSnowball(self, X, Y):
		self.gameSocket.Send('%xt%s%u#sb%-1%' + str(X) + '%' + str(Y) + '%', False)
		
	def SendEmote(self, emoteId):
		self.gameSocket.Send('%xt%s%u#se%-1%' + str(emoteId) + '%', False)
		
	def SendJoke(self, jokeId):
		self.gameSocket.Send('%xt%s%u#sj%-1%' + str(jokeId) + '%', False)
		
	def SetParameter(self, parameterName, parameterValue):
		self.gameSocket.Send('%xt%s%oasis#setpa%-1%' + parameterName + '%' + parameterValue + '%', False)
		
	def LikeUser(self, playerId):
		self.gameSocket.Send('%xt%s%oasis#like%-1%' + str(playerId) + '%', False)