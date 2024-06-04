# Exercicios Python Estruturado

# Implementar uma solução em Python que receba dois números e identifique qual o maior deles
#Estraegia 01
a = 10
b = 20
if (a>b):
    maior = a
else:
    maior = b
print(f'O maior número é: {maior}')

# Implementar uma solução em Python que verifique se um número é par ou ímpar
numero = 46
if(numero%2==0):
    situacao="O número é par"
else:
    situacao="O número é ímpar"
print(situacao)

# Se a nota for maior ou igual a 7, o estudando foi aprovado
# Se a nota for menor que 7 e maior ou igual a 5, o estudante está em recuperação
# Se a nota for menor que 5, o estudando está reprovado
media = 8.5
if(media>=7.0):
    situacao = "aprovado"
elif(media>=5.0):
    situacao = "em recuperação"
else:
    situacao = "reprovado"
print(f'O estudante está: {situacao}')

#Calcular o valor de uma compra, sendo que o preço unitário é 10,00
#Se for feita uma compra de até 10 unidades, não há descontos
#Para compra entre 11 e 20 unidades é dado um desconto de 10%
#Acima de 0 unidades, é dado um desconto de 20%
preco_unitario = 10
desconto10 = 0.1
desconto20 = 0.2
quantidade = eval(input("Digite a quantidade que vai comprar: "))
if(quantidade <=10):
    valor_final = preco_unitario*quantidade
elif(quantidade <= 20):
    valor_final = preco_unitario*quantidade*(1-desconto10)
else:
    valor_final = preco_unitario*quantidade*(1-desconto20)
print(f'O valor final da compra é: {valor_final}')

#Implementar uma solução que some todos os números pares de uma lista
# lista {10, 2, 5, 7, 6, 3}, o resultado deve ser igual a 18
#Estrategia 01
lista = [10, 2, 5, 7, 6, 3]
n=len(lista)
soma=0
for i in range(n):
    if(lista[i]%2==0):
        soma=soma+lista[i]
print(f'O somatório dos elementos pares da lista é: {soma}')

#Estrategia 02 - Funcional
lista = [10, 2, 5, 7, 6, 3]
soma=0
for num in lista:
    if(num%2==0):
        soma=soma+num
print(f'O somatorio dos elementos pares da lista é: {soma}')













