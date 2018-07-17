from create_product_partitions_class import Create_Product_Partitions
from itertools import product

def add_elements(a,b,map_list):
	map_length = len(map_list)
	result = [(a[x]+b[x])%map_list[x] for x in range(map_length)]
	return result

def list_2_num(a,map_list):
	running_product = 1
	number = a[0]
	map_length = len(map_list)
	for map_position in range(1,map_length):
		running_product *= map_list[map_position-1]
		number += a[map_position]*running_product
		
	return number
		
order = 4
prodpart = Create_Product_Partitions(order)
partitions = prodpart.partitions()
print partitions
for partition_number in range(len(partitions)):
	print partition_number
	print partitions[partition_number]
	range_list = []
	for i in partitions[partition_number]:
		range_list.append(range(i))

	element_list = list(product(*range_list))

	elements = [0 for x in range(order)]
	for i in element_list:
		number = list_2_num(i,partitions[partition_number])
		elements[number] = i
	

	addition_table = [[0 for x in range(order)] for y in range(order)]
	for x in range(order):
		for y in range(order):
			addition_table[x][y] = list_2_num(add_elements(elements[x],elements[y],partitions[partition_number]),partitions[partition_number])
		
#	for row in addition_table:
#		print row
	fourwise_count = [0 for x in range(order)]
	for i in elements:
	
		add1 = add_elements(i,i,partitions[partition_number])
		add2 = add_elements(i,i,partitions[partition_number])
		result = list_2_num(add_elements(add1,add2,partitions[partition_number]),partitions[partition_number])
		fourwise_count[result] += 1
	print fourwise_count
	raw_input("Enter to continue")
