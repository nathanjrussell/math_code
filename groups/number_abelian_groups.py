def get_partition_list(n):
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
    	return partition_list[n]

def prime_factor_dict(n):
	pf_dict = {}
	d = 2
	while d**2 <= n:
		while (n % d) == 0:
			if d not in pf_dict:
				pf_dict[d] = 0
            		pf_dict[d]+=1  
            		n /= d
        	d += 1
    	if n > 1:
       		if n not in pf_dict:
           		pf_dict[n] = 0
       		pf_dict[n] += 1
 	return pf_dict

def number_of_abelian_groups(n):
	pf_dict = prime_factor_dict(n)
	prod_part = 1
	for p in pf_dict:
		prod_part *= len(get_partition_list(pf_dict[p]))
	return prod_part

for j in range(1,2000):
	print j, number_of_abelian_groups(j)
