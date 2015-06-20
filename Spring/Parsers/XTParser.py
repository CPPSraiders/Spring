class XTParser:
	def returnHandler(self, xtPacket):
		if(self.isValid(xtPacket)):
			arrPacket = self.ParseRaw(xtPacket)
			try:
				return arrPacket[0]
			except:
				return False
	
	def isValid(self, xtPacket):
		if(xtPacket[:4] == "%xt%"):
			return True
		else:
			return False
			
	def ParseRaw(self, xtPacket):
		arrPacket = xtPacket.split('%')
		arrPacket.pop(0)
		arrPacket.pop(0)
		arrPacket.pop()
		return arrPacket