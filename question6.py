'''take a space separated input from a user and print alternate elements


 take list of elements  


count even and odd elements  
   
l=list(map(int,input().split(" ")))
for i in range(0,len(l),2):
   print(l[i])
'''


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
