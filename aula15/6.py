def fun(a):
    if a > 0:
        print(f"{a} é positivo")
    else a < 0:
        print(f"{a} é negativo")

num = int(input("Informe um número: "))
fun(num)
