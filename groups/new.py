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

multiplication_table = [[0,0,0,0],[0,0,1,1],[0,1,2,3],[0,1,3,2]]
multiplication_table[3],multiplication_table[2]= multiplication_table[2],multiplication_table[3]
print(partitions)
for partition_number in range(len(partitions)):
	print(partition_number)
	print(partitions[partition_number])
	range_list = []
	for i in partitions[partition_number]:
		range_list.append(list(range(i)))

	element_list = list(product(*range_list))

	elements = [0 for x in range(order)]
	for i in element_list:
		number = list_2_num(i,partitions[partition_number])
		elements[number] = i
	

	addition_table = [[0 for x in range(order)] for y in range(order)]
	for x in range(order):
		for y in range(order):
			addition_table[x][y] = list_2_num(add_elements(elements[x],elements[y],partitions[partition_number]),partitions[partition_number])
	print("ADDITION TABLE")	
	for row in addition_table:
		print(row)
	print("MULTIPLICATION TABLE")
	for row in multiplication_table:
		print(row)
	distributive_possibilities = list(product(list(range(4)),list(range(4)),list(range(4)),list(range(4))))
#	for i in range(4):
#		for j in range(4):
#			for k in range(4):
#				singlesum = addition_table[j][k]
#				singleproduct = multiplication_table[i][singlesum]
#				firstproduct = multiplication_table[i][j]
#				secondproduct = multiplication_table[i][k]
#				doublesum = addition_table[firstproduct][secondproduct]
#				if singleproduct != doublesum:
#					print i,j,k, singleproduct,doublesum
#					raw_input("OOPS")
#	fourwise_count = [0 for x in range(order)]
#	for i in elements:
	
#		add1 = add_elements(i,i,partitions[partition_number])
#		add2 = add_elements(i,i,partitions[partition_number])
#		result = list_2_num(add_elements(add1,add2,partitions[partition_number]),partitions[partition_number])
#		fourwise_count[result] += 1
#	print fourwise_count
	input("Enter to continue")
