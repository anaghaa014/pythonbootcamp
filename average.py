name=input("enter your name\n")
sub1=int(input("enter your marks in english\n"))
sub2=int(input("enter your marks in hindi\n"))
sub3=int(input("enter your marks in science\n"))
sub4=int(input("enter your marks in social\n"))
sum=0
sum=sub1+sub2+sub3+sub4
avg=sum/4
print(f"hello {name} your total is {sum} your average is {avg}")
english,hindi,science,social=map(int,input().split())
sum=english+hindi+science+social
print(f"marks are {sum} and average {sum/4}")