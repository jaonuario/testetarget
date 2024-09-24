sequencia = input("entrada->")

a_cont = 0
for letra in sequencia:
    if letra == 'A' or letra == 'a':
        a_cont += 1

print("Há", a_cont, "'a' na sua string")