'''print even numbers from 1 to 10
you are given comma separated numbers'''
l=list(map(int,input().split(",")))
count=0
for i in range(1,len(l),2):
   count+=1
   print(l[i])
print(count)

'''how many even numbers are there in the above question'''
'''count is used to resolve it'''

