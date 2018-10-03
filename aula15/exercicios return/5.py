def calc(a, b, c):
    x = (a * b) + c
    return x

distancia = int(input("Distância (Km): "))
value = float(input("Valor por Km (R$): "))
b = float(input("Bandeirada (R$): "))

preco = calc(distancia, value, b)
print(preco)
