class Board:

	
	def __init__(self):
		self.config = [[0 for x in xrange(15)] for x in xrange(15)] 

	def toString(self):
		rtn="-------------------------------"
		for j in range(15):
			rtn+="\n"+"|"
			for i in range(15):
				pos = self.config[i][j]
				if pos==0:
					pos=" "

				rtn+=str(pos)+"|"
		rtn+="\n-------------------------------"
		return rtn