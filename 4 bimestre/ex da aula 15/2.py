def funcao():
    nome = input("Nome: ")
    idade = int(input("Idade: "))

    if idade >= 18:
        print(nome, "maior de idade")
    else:
        print(nome, "menor de idade")

funcao()
