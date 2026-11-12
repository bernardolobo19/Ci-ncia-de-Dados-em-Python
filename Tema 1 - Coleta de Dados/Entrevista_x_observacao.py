import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Simulando dados de entrevistas para 100 participantes
np.random.seed(42)
dados_entrevistas = {
    'Participante': np.arange(1, 101),
    'Satisfação_Entrevista': np.random.choice(['Alta', 'Média', 'Baixa'], size=100),
    'Idade': np.random.randint(18, 60, size=100),
    'Tempo_Entrevista': np.random.randint(10, 60, size=100)
}

# Simulando dados de entrevistas para 80 participantes

dados_observacao = {
    'Participante': np.arange(1, 81),
    'Satisfação_Observação': np.random.choice(['Alta', 'Média', 'Baixa'], size=80),
    'Tempo_Observação': np.random.randint(10, 60, size=80)
}

# Conversão para DataFrame
df_entrevistas = pd.DataFrame(dados_entrevistas)
df_observacao = pd.DataFrame(dados_observacao)

# Unindo os dois DataFrames com base nos Participantes

df = pd.merge(df_entrevistas, df_observacao, on='Participante', how='left')

# Cálculo da proporção das respostas de satisfação para entrevistas e observação

satisfacao_entrevista = df['Satisfação_Entrevista'].value_counts(normalize=True).mul(100).reset_index()
satisfacao_entrevista.columns = ['Satisfação', 'Percentual Entrevista']

satisfacao_observacao = df['Satisfação_Observação'].value_counts(normalize=True).mul(100).reset_index()
satisfacao_observacao.columns = ['Satisfação', 'Percentual Observação']

# Unindo as duas proporções

df_comparacao = pd.merge(satisfacao_entrevista, satisfacao_observacao, on='Satisfação', how='outer').fillna(0)

# Definindo a ordem correta das categorias no eixo X

ordem_satisfacao = ['Baixa', 'Média', 'Alta']
df_comparacao['Satisfação'] = pd.Categorical(df_comparacao['Satisfação'], categories=ordem_satisfacao, ordered=True)

# Visualização com seaborn
plt.figure(figsize=(10, 6))
sns.set_style("whitegrid")

# Gráfico de barras lado a lado com cores vibrantes
df_comparacao = df_comparacao.sort_values(by='Satisfação')
df_comparacao.plot(kind='bar', x='Satisfação', y=['Percentual Entrevista', 'Percentual Observação'],
                    color=['#FF5733', '#33FF57'], edgecolor='black', width=0.8)

# Ajustes de títulos e eixo
plt.title('Comparação Percentual de Satisfação entre Entrevistas e Observações', fontsize=16)
plt.xlabel('Nível de Satisfação', fontsize=12)
plt.ylabel('Percentual (%)', fontsize=12)
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()