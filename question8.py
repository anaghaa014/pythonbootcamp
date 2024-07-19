'''you are given with a space separated integer list.
find num of even elements and num of odd elements in the given list'''

l=list(map(int,input().split(" ")))
ecnt=0
ocnt=0
for i in range(len(l) ):
   if(i%2==0):
      ecnt+=1

   else:
        ocnt+=1
print(ecnt)
print(ocnt)
