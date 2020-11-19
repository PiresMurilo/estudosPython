x = int(input("digite a largura: "))
y = int(input("digite a altura: "))
largura = 1
altura = 1
while altura <= y:
    while largura <= x:
        print("#", end = "")
        largura = largura + 1
    altura = altura + 1
    print()
    largura = 1

linha = 1

# Enquanto houver linha a ser exibida:
while  linha <= altura:

    print("#", end = "")
    coluna = 2

    # Substituído linha por largura também
    while coluna < largura: 

        # Se for a primeira linha, a última ou a última coluna
        if linha == 1 or linha == altura or coluna == largura:
            print("#",end="")
        else:
            print(end = " ")

        coluna = coluna + 1

    print("#")

    # Incrementa a variável linha ao invés de decrementar altura
    linha = linha + 1