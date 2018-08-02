from create_product_partitions_class import Create_Product_Partitions
from itertools import product
from pyeda.inter import *

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

#multiplication_table = [[0,0,0,0],[0,0,1,1],[0,1,2,3],[0,1,3,2]]
#multiplication_table = [[0,0,0,0],[0,1,0,1],[0,0,2,2],[0,1,2,3]]
#multiplication_table = [[0,0,0,0],[0,1,2,3],[0,2,3,1],[0,3,1,2]]
multiplication_table = [[0,0,0,0],[0,1,2,3],[0,2,0,2],[0,3,2,1]]


print(partitions)
partition_number=0
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
	
result1 = [0 for x in range(32)]
result2 = [0 for x in range(32)]
for operation in range(2):
	for element2 in range(4):
		for element1 in range(4):
			if operation==1:
				output = multiplication_table[element1][element2]
			else:
				output = addition_table[element1][element2]
			#print("{0!s},{1!s},{2!s},{3!s},{3:02b},{4!s}".format(element1,element2,operation,output,bin(output)[2:].zfill(2)[1]))
			binstring = "{2:b}{1:02b}{0:02b}".format(element1,element2,operation)
			intresult = int(binstring,2)
			#print(int(binstring,2))
			print(operation,element2,element1,binstring,output,bin(output)[2:].zfill(2)[0],bin(output)[2:].zfill(2)[1])

			result1[intresult] = bin(output)[2:].zfill(2)[0]
			result2[intresult] = bin(output)[2:].zfill(2)[1]
X = ttvars('x',5)
f1 = truthtable(X,"".join(result1))
f2 = truthtable(X,"".join(result2))
f1m = espresso_tts(f1)
f2m = espresso_tts(f2)
print(f1m)
print(f2m)
