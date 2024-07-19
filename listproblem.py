'''my_list=list(map(int,input().split("@")))
my_list=list(map(str,input().split(" ")))
print(*my_list)'''

my_list=list(map(int,input().split(" ")))
print("Enter 1 for appending new element")
print("Enter 2 for deleting the element")
print("Enter 3 for  sorting the elements")
print("Enter 4 for printing the length")
choice=int(input())
if(choice==1):
    print(f"my_list+append(81)")
elif(choice==2):
    print(f"my_list.pop()")
elif(choice==3):
    print(f"my_list.sort()")
elif(choice==4):
    print(f"good morning,{(my_list)}")
else:
    print(f"enter correct choice")
