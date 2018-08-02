from prime_fact_dict import Prime_Fact_Dict
from create_partitions import Create_Partitions
from itertools import product

class Create_Product_Partitions(object):
	def __init__(self,number=1):
		self.number = number
		self.product_partitions = []
		temp_pf_dict = Prime_Fact_Dict(self.number).factorization_dict()
		
		prime_list = []
		exp_list = []
		for p in temp_pf_dict:
			prime_list.append(p)
			partlist = Create_Partitions(temp_pf_dict[p]).possible_partitions()
			exp_list.append(partlist)
			
		possible_exponent_maps = list(product(*exp_list))
		for exponent_map in possible_exponent_maps:
			candidate_list = []
			for prime_position in range(len(prime_list)):
				for exponent in exponent_map[prime_position]:
					candidate_list.append(prime_list[prime_position]**exponent)

			candidate_list.sort()
			self.product_partitions.append(candidate_list)

	def partitions(self):
		return self.product_partitions

