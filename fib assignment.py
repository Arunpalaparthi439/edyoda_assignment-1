a = int(input("enter a number :"))
b = 0
c = 1
sum = 0
for i in range(0, a):
    if a<=0:
        print("enter number greater than 0")
    else:
        print(sum , end=" ")
        b = c
        c = sum
        sum = b + c

