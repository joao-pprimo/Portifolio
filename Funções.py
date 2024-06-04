# Implementar uma solução em Python que retorno o menor elemento de uma lista
lista_teste = [2, 10, 3, 1, 4, 5]
def encontrar_minimo(lista):
    minimo = lista[0]
    for elem in lista:
        if(elem < minimo):
            minimo = elem
    return minimo
menor = encontrar_minimo(lista_teste)
print('O menor elemento da lista é: [{}]'.format(menor))

# Exercicio 1
# Implementar uma solução em Python que retorne a soma de todos os elementos pares de uma lista
lista = [10, 2, 5, 7, 6, 3]
def ehPar(n):
    r = (n%2==0)
    return r
def soma_par(lst):
    soma=0
    for num in lst:
        if(ehPar(num)):
            soma = soma+num
    return soma
soma=soma_par(lista)
print(f'O somatorio dos elementos pares da lista é: {soma}')

# Exercicio 2
# Implementar uma solução em Python que calcule o fatorial de um número
numero = 5
#Estrategia 01
def fatorial_iterativo(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
#Estrategia 02
def fatorial_recursivo(n):
    if((n==0)or(n==1)):
        return 1
    return n*fatorial_recursivo(n-1)
print(f'O fatorial de {numero} é: {fatorial_iterativo(numero)}')
print(f'O fatorial de {numero} é: {fatorial_recursivo(numero)}')

# Exercicio 3
# Implementar uma solução em Python que determine se um número é ou não primo
numero = 7
def eh_primo(n):
    if(n<2):
        return False
    i=n//2
    while(i>1):
        if(n%i==0):
            return False
        i=i-1
    return True
def imprimir_resultado(numero, resultado):
    mensagem= f'O número {numero} NÃO é primo'
    if(resultado):
        mensagem= f'O número {numero} é primo'
    return mensagem
resultado=eh_primo(numero)
msg=imprimir_resultado(numero, resultado)
print(msg)

















