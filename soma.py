print("Digite uma sequência de números a serem somados, ao terminar digite 0 ")

valor = 1
soma = 0
while valor != 0:
    valor = int(input("Digite um valor a ser somado: "))
    soma = valor + soma

print("A soma dos valores digitados é:", soma)
