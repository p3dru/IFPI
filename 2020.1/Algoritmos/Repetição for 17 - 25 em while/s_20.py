denominador_final = int(input("Digite um número: "))
numerador = contador = 1
total = 0
while contador <= denominador_final:
    if contador % 2 != 0:
        total += numerador / contador
        contador += 1
    else:
        total -= numerador / contador
        contador += 1
print(f"O valor final de s é: {total:.2f}")
