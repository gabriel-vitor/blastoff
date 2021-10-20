def imprimeMatriz(matriz):
    for lin in range(0, 2):
        for col in range(0,3):
            print(f'[{matriz[lin][col]}]', end = '')
        print()
    
    
matriz = [[0, 0, 0], [0, 0, 0]]
for lin in range(0, 2): #linha
    for col in range(0,3): #coluna
        matriz[lin][col] = int(input(f'digite um valor [{lin}, {col}]:'))
        
print(imprimeMatriz(matriz))
    