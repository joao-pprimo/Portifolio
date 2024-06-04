# Exemplo 1 - Número par ou não
# Implementar uma solução em Python que faça o tratamento da exceção para verificar
# Se a entrada é, de fato, um número
try:
    x = int(input('Digite um número: '))
except ValueError:
    print('Entre com um número válido.')
#Exercicio
#Implementar uma solução em Python que faça o tratamento de exceção para verificar se
while True:
    try:
        x = int(input('Digite um número: '))
        break
    except ValueError:
        print('Entre com um número válido.')

# Exercicio 02
# Implementar uma solução em Python que faça o tratamento de exceção de divisão por Zero.
def dividir(x, y):
    try:
        resultado = x / y
        print('A resposta é: ', resultado)
    except ZeroDivisionError:
        print('Divisão por zero')
dividir(3, 0)
dividir(3, 2)

# KeyboardInterrupt	Levantado quando o usuário pressiona CTRL+C, a combinação de interrupção.
# OverflowError	Levantado quando uma expressão de ponto flutuante é avaliada como um valor muito grande.
# ZeroDivisionError	Levantado quando se tenta dividir por 0.
# IOError	Levantado quando uma operação de entrada/saída falha por um motivo relacionado a isso.
# IndexError	Levantado quando um índice sequencial está fora do intervalo de índices válidos.
# NameError	Levantado quando se tenta avaliar um identificador (nome) não atribuído.
# TypeError	Levantado quando uma operação da função é aplicada a um objeto do tipo errado.
# ValueError	Levantado quando a operação ou função tem um argumento com o tipo correto, mas valor incorreto.



