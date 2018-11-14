def li():
    L=[]
    q= int(input("Informe a quantidade de elementos: "))
    for i in range(0, q):
        n= int(input("Informe um número inteiro: "))
        L.append(n)
    return L
x=li()
print(x)
    
