class Prime_Fact_Dict(object):
	def __init__(self,number=1):
		self.number = number
		n = self.number
		self.pf_dict = {}
		d = 2
		while d**2 <= n:
			while (n % d) == 0:
				if d not in self.pf_dict:
					self.pf_dict[d] = 0
				self.pf_dict[d]+=1
				n /= d
			d += 1
		if n > 1:
			if n not in self.pf_dict:
				self.pf_dict[n] = 0
			self.pf_dict[n] += 1
 	
	def factorization_dict(self):
		return self.pf_dict

	def get_number(self):
		return self.number
