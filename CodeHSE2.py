#задание 2
a=int(input(">>> "))
b=int(input(">>> "))
for i in range(a, b+1):
    s=str(i)
    n=str(i)[::-1]
    if s == n:
        print(s)
input()