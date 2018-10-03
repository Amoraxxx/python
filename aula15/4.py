def fun(nome, idade):
    if idade >= 18:
        print(nome, "é maior de idade")
    else:
        print(nome, "é menor de idade")

a = input("Seu Nome: ")
b = int(input("Sua Idade: "))
fun(a,b)
