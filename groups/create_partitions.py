class Create_Partitions(object):
	def __init__(self,number=1):
		self.number = number
		n = self.number
		partition_list= []
		partition_list.append([[]])
		partition_list.append([[1,]])
		for k in range(2, n+1):
			partitions = []
			for i in range(k):
				for partition in partition_list[i]:
					tmp_list = list(sorted([k-i] + partition))
					if tmp_list not in partitions:
						partitions.append(tmp_list)
			partition_list.append(partitions)
		self.partitions = partition_list[n]
	
	def possible_partitions(self):
		return self.partitions

	def get_number(self):
		return self.number
