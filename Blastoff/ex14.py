palavra = input("Digite uma palavra ")
if palavra == "".join(reversed(palavra)) :
    print("É palindromo")
else:
    print("Não é palindromo")