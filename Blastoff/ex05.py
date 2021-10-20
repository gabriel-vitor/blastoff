num1 = int(input("informe o primeiro número: "))
num2 = int(input("informe o segundo número: "))

if num1>num2:
    if num1 % num2 != 0:
        print("não são múltiplos")
    else:
        print("são multiplos")
else:
    if num2 % num1 != 0:
        print("não são multiplos")
    else:
        print("são múltiplos")
