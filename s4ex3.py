inteiro = int(input("Digite um número inteiro: "))

soma = 0
while inteiro > 0:
    u = inteiro % 10
    inteiro = inteiro // 10
    soma = soma + u

print(soma)

