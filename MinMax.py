def MinMax(temperaturas):
    print("A menor temperatura do mês foi:", minima(temperaturas), "C.")
    print("A maior temperatura do mês foi:", maxima(temperaturas), "C.")

def minima(temps): #algorimto seguido sera com o WHILE mas poderia ser com um FOR
    min = temps[0]
    i = 1
    while i < len(temps):
        if temps[i] < min:
            min = temps[i]
        i = i + 1
    return min

def maxima(temps):
    max = temps[0]
    i = 1
    while i < len(temps):
        if temps[i] > max:
            max = temps[i]
        i = i + 1
    return max

#TESTES AUTOMATIZADOS

def teste_pontual(temp, valorEsperado):
    minima(temp) = valorCalculado
    if valorCalculado != valorEsperado:
        print("Valor errado para array: ", temp)
        print("O valor esperado é: " valorEsperado, ".O valor calculado", valorCalculado)

####################
def testa_minima():
    print("Iniciando os testes")
    
    teste_pontual([0], 0)
    teste_pontual([0, 0, 0], 0)
    teste_pontual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0)
    teste_pontual([-15, -12, -2, 0, 20, 30], -15)

    print("Finalizando os testes")