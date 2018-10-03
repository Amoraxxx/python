def fun():
    nom = input("Seu Nome: ")
    idad = int(input("Sua Idade: "))

    if idad <= 18:
        print(nom, "é menor de idade")
    else:
        print(nom, "é maior de idade")

func()
