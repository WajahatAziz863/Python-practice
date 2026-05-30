n=int(input("enter 1st number:"))
m=int(input("enter 2nd number:"))
p=int(input("enter 3rd number:"))
if n >= m and n >= p:
    largest = n
elif m >= n and m >= p:
    largest = m
else:
    largest = p
print("Largest is:",largest)