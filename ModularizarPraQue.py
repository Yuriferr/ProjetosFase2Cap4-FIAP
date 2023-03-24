import ModularPraQueCalculadora
from ModularPraQueCalculadora import somar
from ModularPraQueCalculadora import *

op = -1

while op != 5:
    print("1 - Somar \n2 - Subtrair \n3 - Dividir \n4 - Multiplicar \n5 - Sair")
    op = int(input("Digite a sua Opcao: "))
    if op == 1:
        print(somar(float(input("Digite o primeiro valor: ")), float(input("Digite o segundo valor: "))))
    elif op == 2:
        print(subtrair(float(input("Digite o primeiro valor: ")), float(input("Digite o segundo valor: "))))
    elif op == 3:
        print(dividir(float(input("Digite o primeiro valor: ")), float(input("Digite o segundo valor: "))))
    elif op == 4:
        print(multiplicar(float(input("Digite o primeiro valor: ")), float(input("Digite o segundo valor: "))))
