# Crie um programa que receba um número do usuário e exiba a tabuada desse número de 1 a 10.
def mostrar_tabuada(numero):
    print(f"Tabuada do {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

def main():
    numero = int(input("Digite um número para ver a tabuada: "))
    mostrar_tabuada(numero)

main()
