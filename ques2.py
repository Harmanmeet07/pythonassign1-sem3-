a=[]
b=[]
n1=int(input("Enter the number of elements:"))
for l in range(0,n1):
    element1=int(input())
    a.append(element1)
print(a)

n2=int(input("Enter the number of elements:"))
for l in range(0,n2):
    element2=int(input())
    b.append(element2)
print(b)

final_arr=a+b
print(final_arr)
