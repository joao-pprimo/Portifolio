# Imports
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Carrega os dados
df_dsa = pd.read_csv('dados/dados_clientes.csv')
type(df_dsa)

# Visualiza as 10 primeiras linhas
df_dsa.head(10)

# Análise Exploratória
# Resumo estatístico
df_dsa[['idade', 'renda_anual', 'pontuacao_gastos']].describe()

# Pré-Processamento dos Dados

# Cria o padronizador dos dados
padronizador = StandardScaler()
# Aplica o padronizador somente nas colunas de interesse
dados_padronizados = padronizador.fit_transform(df_dsa[['idade', 'renda_anual', 'pontuacao_gastos']])

# Visualiza os dados
print(dados_padronizados)

Construção do Modelo de Machine Learning Para Segmentação de Clientes
# Definimos o número de clusters (k)
k = 3
# Criamos o modelo K-means
kmeans = KMeans( n_clusters = k)
# Treinamento do modelo com os dados padronizados
kmeans.fit(dados_padronizados)
# Atribuímos os rótulos dos clusters aos clientes
df_dsa['cluster'] = kmeans.labels_
# Exibe o resultado (10 primeiras linhas)
df_dsa.head(10)
# Salvamos o resultado em disco
df_dsa.to_csv('dados/segmentos.csv', index = False)

# Instala o pacote
!pip install -q powerbiclient
# Carrega as funções usadas para autenticar e gerar  relatórios
from powerbiclient import QuickVisualize, get_dataset_config, Report
from powerbiclient.authentication import DeviceCodeLoginAuthentication

# Define a autenticação no Power BI Service
device_auth = DeviceCodeLoginAuthentication()
# Cria o relatório no Power BI
relatorio_PBI = QuickVisualize(get_dataset_config(df_dsa), auth = device_auth)
