def funcao(nome, idade):
    if idade >= 18:
        print(nome, "maior de idade")
    else:
        print(nome, "menor de idade")

a = input("Nome: ")
b = int(input("Idade: "))
funcao(a,b)
