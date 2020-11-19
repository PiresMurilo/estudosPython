i = int(input("Digite um número inteiro: "))
produto = 1
u = 1
if i == 0:
    print("Nem foi realizado todo o calculo pois qualquer número multiplicado por 0 é 0")

else:
    while i > 0:
        u = i % 10
        i = i // 10
        produto = u * produto

print("O produto dos algarismos é", produto)