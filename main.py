## Primeiro comentário

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
    else:
        print("Operação inválida")

    return result


if __name__ == "__main__":

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        try:
            print('Calculadora')
            print('----------------------------------\n')


        except ValueError:
            print('Dados inválidos! -> Tente novamente!')
            time.sleep(2)

        except ZeroDivisionError:
            print('Impossível dividir por zero! -> Tente novamente!')
            time.sleep(2)

    print('\nVolte sempre!\n')
    
    
    
    """ 
4º Efetuar as alterações necessárias fazendo vários commits e push
5º Têm de terminar a implementação de uma calculadora
No bloco principal deverão implementar uma forma de solicitar 2 numeros ao utilizador e o tipo de operação a realizar.
Após exibição do resultado deverão perguntar se o utlizador deseja continuar a efetuar mais operações
As operações a implementar serão a soma, subtração, divisão, multiplicação e exponenciação
 
6º Ir ao github verificar as alterações e partilhar o link do repositório na tarefa"""
