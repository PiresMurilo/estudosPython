numero = int(input("Digite o número: "))
anterior = numero - 1
fatorial = numero * anterior

if numero < 0:
  fatorial(n) == False

else:
    if numero <= 1:
        print("1")

    else: 
        while anterior != 1:
            anterior = anterior - 1
            fatorial = fatorial * anterior

print (fatorial)