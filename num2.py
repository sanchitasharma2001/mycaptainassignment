list1=[]
list2=[]
n=int(input("Enter number of elements for list 1:"))
print("Enter numbers")
for i in range (0,n):
    ele=int(input())
    list1.append(ele)
n2=int(input("Enter number of elements for list 2:"))
print("Enter numbers")
for i in range (0,n2):
    ele=int(input())
    list2.append(ele)
for n in list1:
         if n>=0:
              print("positive numbers in list1:")
              print(n)
for n2 in list2:
         if n2>=0:
              print("positive numbers in list2:")
              print(n2)
