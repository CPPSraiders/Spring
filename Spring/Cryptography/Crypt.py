from hashlib import md5

class Crypt:
	def getLoginHash(self, password, randomKey):
		hash  = self.encryptPassword(password).upper()
		hash += randomKey
		hash += 'Y(02.>\'H}t":E1'
		hash  = self.encryptPassword(hash)
		return hash
		
	def getGameHash(self, randomKey, playerKey, playerConfirm):
		hash  = self.encryptPassword(playerKey + randomKey)
		hash += playerKey
		hash += '#'
		hash += playerConfirm
		return hash
		
	def encryptPassword(self, password, nMd5 = True):
		if(nMd5):
			password = md5(password).hexdigest()
		
		return self.swapHash(password)
		
	def swapHash(self, password):
		return password[16:] + password[:16]