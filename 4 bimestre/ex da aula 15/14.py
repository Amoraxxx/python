def cal(a, b, c):
    pag = (a * b)+ c
    print(f"A corrida custou R${pag}")


tancia = int(input("Distância percorrida (Km): "))
cus = float(input("Custo por Km (R$): "))
b = float(input("Valor da bandeirada (R$): "))

cal(tancia,cus,b)
