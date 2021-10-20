quantidade = 5 #são cinco alunos I, J, K, X, Y
i=0
soma = 0
while i < quantidade:
    idade = int(input("informe a idade do aluno: "))
    soma = soma + idade
    i += 1;
media = soma / quantidade
print("A média das idades é:", media)