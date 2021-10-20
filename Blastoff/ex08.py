num = int(input("Digite um número"))
divisoes = 0

n=1

while n < (num + 1):
    if (num % n) == 0:
        divisoes += 1
    n += 1
# um numero primo só é divisivel por 1 eele mesmo
if divisoes < 3:
    print("é número primo")
else:
    print("não é número primo")