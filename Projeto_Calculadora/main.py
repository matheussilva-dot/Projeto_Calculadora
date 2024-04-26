print("Calculadora Simples")

def calcular():
    while True:
        try:

            operacao = input("Digite a operação desejada: +, -, *, /, ** ")

            if operacao not in ['+', '-', '*', '/', '**']:
                raise ValueError("Operação inválida.")
            

            v1 = float(input("Digite o 1º valor: "))
            v2 = float(input("Digite o 2º valor: "))

            if operacao == '/' and v1 == 0 or v2 == 0:
                raise ValueError("Divisão por zero não permitida!")

            res1 = v1 + v2
            res2 = v1 - v2
            res3 = v1 * v2
            res4 = v1 / v2
            res5 = v1 ** v2



            if operacao == "+":
                print(f"O Resultado é: {res1}")
            elif operacao == "-":
                print(f"O Resultado é: {res2}")
            elif operacao == "*":
                print(f"O Resultado é:{res3}")
            elif operacao == "/":
                print(f"O Resultado é:{res4}")
            elif operacao == "**":
                print(f"O Resultado é:{res5}")
            else:
                print("Digitou a operação errada")

            contunuar = input("Deseja continuar (s/n): ")
            
            if contunuar.lower() != "s":
                break
                    

        except ValueError as e:
            print(f'Erro: {e}')

        except Exception as e: 
            print(f'Erro inesperado: {e}')

calcular()

