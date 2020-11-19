inteiro = int(input("Digite o valor de n: "))
ultimo = inteiro % 10
restante = inteiro // 10

soma = 0
while ultimo != 0:
    if ultimo > 0:
        ultimo = inteiro % 10
        restante = inteiro // 10
        soma = soma + ultimo

print (soma)
