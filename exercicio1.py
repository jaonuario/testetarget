numero = int(input("entrada->"))

anterior = 0
fibo = 1

while fibo < numero:
    aux = fibo
    fibo = fibo + anterior
    anterior = aux

if numero == fibo:
    print("O numero pertence a sequencia de fibonacci")
else:
    print("O numero não pertence a sequencia de fibonacci")

