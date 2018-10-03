def fun(a):
    if a > 0:
        print(f"{a} é positivo")
    elif a < 0:
        print(f"{a} é negativo")
    else:
        print(f"{a} é igual a 0")

num = int(input("Informe um número: "))
fun(num)
