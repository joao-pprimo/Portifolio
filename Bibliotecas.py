# Exemplos
# Implementar uma solução em Python que calcule as raízes de uma equação do segundo grau
# Dada a equação x^2 + 5x + 6 = 0, as raízes são {-3, -2}
import numpy as np
def calcular_raizes(a,b,c,delta):
    if(delta<0):
        resultado='a equação não possui raízes nos números reais'
    elif(delta==0):
        x=-b/(2*a)
        resultado=f'a equação possui apenas a raiz: {x}'
    else:
        x1=(-b-np.sqrt(delta))/(2*a)
        x2=(-b+np.sqrt(delta))/(2*a)
        resultado=f'a equação possui as raízes: {x1}, {x2}'
    return resultado
def entrada_dados():
    coeficiente = quantidade = eval(input("Digite o valor do coeficiente: "))
    return coeficiente
def calc_delta(a,b,c):
    delta=b*b-4*a*c
    return delta
# f(x)=ax^2+bx+c
a=entrada_dados()
b=entrada_dados()
c=entrada_dados()

delta=calc_delta(a,b,c)

resultado=calcular_raizes(a,b,c,delta)
print(resultado)

# Exercicio 01
# Implementar uma solução em Python para visualizar dados de vendas de produtos em um gráfico de barras
# Utilize os seguintes dados: x=["A","B","C","D"] y=[3,8,1,10]
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A","B","C","D"])
y = np.array([3, 8, 1, 10])

plt.bar(x,y)
plt.show()

#Implementar uma solução em Python para gerar 1000 pontos seguindo a distribuição Normal com média 20 e desvio-padrao 2.
# Além disso, exiba os dados em um histrograma
import matplotlib.pyplot as plt
import numpy as np
np.random.seed(1)
dados = np.random.normal(loc=20, scale=2, size=1000)
plt.hist(dados, color = "lightblue", ec="red")





























