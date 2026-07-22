def adicao(num, num2):
    return num + num2


def subtracao(num, num2):
    return num - num2


def multiplicacao(num, num2):
    return num * num2


def divisao(num, num2):
    return num / num2


while True:
    print("\n===== CALCULADORA =====")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    operador = input("Qual operação você quer fazer? ")

    if operador in ["1", "2", "3", "4"]:

        num = float(input("\nDigite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if operador == "1":
            print(f"\nResultado da adição: {adicao(num, num2)}")

        elif operador == "2":
            print(f"\nResultado da subtração: {subtracao(num, num2)}")

        elif operador == "3":
            print(f"\nResultado da multiplicação: {multiplicacao(num, num2)}")

        elif operador == "4":

            if num2 == 0:
                print("\nNão é possível dividir por zero.")

            else:
                print(f"\nResultado da divisão: {divisao(num, num2)}")

    else:
        print("\nOpção inválida!")

    continuar = input("\nDeseja continuar? (s/n): ").lower()

    if continuar != "s":
        print("\nObrigado por usar a calculadora!")
        break
