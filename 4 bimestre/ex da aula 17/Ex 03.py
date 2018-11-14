L1=[]
L2=[]

q= int(input("Informe a quantidade de elementos: "))
for i in range(0, q):
    n= int(input("Informe um número da L1: "))
    L1.append(n)
for i in range(0, q):
    n= int(input("Informe um número da L2: "))
    L2.append(n)
def li():
    L3=[]
    for i in range (0, len(L1)):
        soma= L1[i] + L2[i]
        L3.append(soma)
    return L3


x= li()
print(x)
    
