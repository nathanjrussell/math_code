#r(And(x[1], ~x[3], ~x[4]), And(~x[1], x[3], ~x[4]), And(x[1], x[3], x[4])),)
#(Or(And(~x[0], x[1], x[2]), And(x[0], ~x[2], ~x[4]), And(~x[0], x[2], ~x[4]), And(x[0], ~x[2], x[3]), And(x[0], ~x[1], x[3], x[4]), And(x[1], x[2], ~x[3], x[4])),)

x = [1,1,0,1,1]
print (x[1] and  not x[3] and  not x[4]) or  (not x[1] and  x[3] and  not x[4]) or (x[1] and  x[3] and  x[4])

print (not x[0] and x[1] and x[2]) or (x[0] and not x[2] and not x[4]) or (not x[0] and  x[2] and not x[4]) or (x[0] and not x[2] and x[3]) or (x[0] and not x[1] and x[3] and x[4]) or (x[1] and x[2] and not x[3] and  x[4])



