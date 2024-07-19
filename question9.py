'''given an space separated integer list
find the average of elements present in the even index'''

l=list(map(int,input().split(" ")))
ecnt=0
total=0
avg=0
for i in range(len(l)):
   if(i%2==0):
      total=total+l[i]
      ecnt+=1
avg=total/ecnt
print(avg)