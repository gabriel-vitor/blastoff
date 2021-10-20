a = int(input("A - informe um número:"))
b = int(input("B - informe um número:"))
c = int(input("C - informe um número:"))

if a < b and a < c:
    print("o menor número é ", a)
elif b < c and b < a:
    print("o menor é", b)
else:
    print("o menor é", c)