# Calculadora simples em Python

import os
import time

def calculadora(num1: float, num2: float, operador: str) -> float:
    """
    Usar nan como valor inicial é uma boa prática. 
    Se o operador fornecido não corresponder a nenhuma das opções válidas (+, -, etc.), a função retornará nan, 
    sinalizando que o cálculo não pôde ser realizado.
    """
    result = float("nan")
    
    if operador == '+':
        result = num1 + num2
    elif operador == "-":
        result = num1 - num2
    elif operador == "*":
        result = num1 * num2
    elif operador == "/":
        result = num1 / num2
    elif operador == "**":
        result = num1 ** num2
    else:
        print("Operação inválida")

    return result


if __name__ == "__main__":

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        try:
            print('Calculadora')
            print('----------------------------------\n')
            #print('Insira o número, o sinal de operação e o segundo número, carregando Enter entre cada inserção.')
            print('Operações disponíveis:')
            print('+  (soma)\n-  (subtração)')
            print('*  (multiplicação)\n/  (divisão)')
            print('** (exponenciação)\n')
            print('----------------------------------\n')
            
            # Solicitar números e operador ao utilizador
            num1 = float(input('Insira o primeiro número: '))
            operador = input('Seguido do operador (+, -, *, /, **): ')
            num2 = float(input('Insira o segundo número: '))
            
            resultado = calculadora(num1, num2, operador)
            print(f"\nResultado: {resultado}")

            continuar = input("\nDeseja continuar? (s/n): ").strip().lower()
            if continuar != 's':
                print('\nVolte sempre!\n')
                break


        except ValueError:
            print('Dados inválidos! -> Tente novamente!')
            time.sleep(2)

        except ZeroDivisionError:
            print('Impossível dividir por zero! -> Tente novamente!')
            time.sleep(2)
    
    
    
    """ 
4º Efetuar as alterações necessárias fazendo vários commits e push
5º Têm de terminar a implementação de uma calculadora
No bloco principal deverão implementar uma forma de solicitar 2 numeros ao utilizador e o tipo de operação a realizar.
Após exibição do resultado deverão perguntar se o utlizador deseja continuar a efetuar mais operações
As operações a implementar serão a soma, subtração, divisão, multiplicação e exponenciação
 
6º Ir ao github verificar as alterações e partilhar o link do repositório na tarefa"""
