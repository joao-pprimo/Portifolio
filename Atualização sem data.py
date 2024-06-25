import pandas as pd

# Carrega a planilha base e a planilha nova
base_df = pd.read_excel('BancoDadosRH - Copia1.xlsx')
nova_df = pd.read_excel('SQL TESTE - Copia.xlsx')

# Remove espaços em branco dos nomes das colunas e converte para maiúsculas
base_df.columns = base_df.columns.str.strip().str.upper()
nova_df.columns = nova_df.columns.str.strip().str.upper()

# Verifica se 'ID' está presente em ambas as planilhas
if 'ID' not in base_df.columns:
    raise KeyError("A coluna 'ID' não foi encontrada na planilha base.")
if 'ID' not in nova_df.columns:
    raise KeyError("A coluna 'ID' não foi encontrada na nova planilha.")

# Convertendo 'ID' para string para evitar problemas de tipo de dados
base_df['ID'] = base_df['ID'].astype(str)
nova_df['ID'] = nova_df['ID'].astype(str)

# Renomeia as colunas da nova planilha para corresponder à planilha base
nova_df.rename(columns={
    'CARGO': 'ID_CARGO',
    'DESCR LOTACAO': 'ID_LOTAÇÃO',
    'CENCUSTO': 'ID_CCUSTO',
    'GRAU DE INSTRUCAO': 'ID_ESCOLARIDADE',
    'DEFICIENCIA': 'ID_DEFICIÊNCIA',
    'SALÁRIO': 'SALARIOS',
    'SITUACAO': 'ID_SITUAÇÃO'
}, inplace=True)

# Adicionar novos colaboradores à planilha base
novos_funcionarios_df = nova_df[~nova_df['ID'].isin(base_df['ID'])]
base_df = pd.concat([base_df, novos_funcionarios_df], ignore_index=True)

# Atualizar a data de demissão na planilha base
for idx, row in nova_df.iterrows():
    id_ = row['ID']
    if id_ in base_df['ID'].values:
        base_index = base_df[base_df['ID'] == id_].index
        if pd.isna(base_df.loc[base_index, 'DT_DEMISSAO']).any() and pd.notna(row['DT_DEMISSAO']):
            base_df.loc[base_index, 'DT_DEMISSAO'] = row['DT_DEMISSAO']

# Salva a planilha base atualizada no mesmo arquivo ou em um novo, conforme necessário
base_df.to_excel('BancoDadosRH - Copia - Atualizada1.xlsx', index=False)

print("Planilha base atualizada com sucesso")
