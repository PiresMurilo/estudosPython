def maior_primo(x):
    aux = x
    while aux > 2:
        if ePrimo(aux):
            return aux
        aux = aux - 1
    return 2


def ePrimo(k):
    i = 2
    while i * i <= k:
        if k % i == 0:
            return False
        i = i + 1
    return True 
