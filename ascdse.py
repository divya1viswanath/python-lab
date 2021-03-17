import operator
d={1:2,3:4,4:3,2:1,0:0}
print('original dictionary:',d)
sorted_d=sorted(d.items(),key=operator.itemgetter(0))
print('dictionary in ascending order by value:',sorted_d)
sorted_d=sorted(d.items(),key=operator.itemgetter(0),reverse=True)
print('dictionary in desending order by value:',sorted_d)
