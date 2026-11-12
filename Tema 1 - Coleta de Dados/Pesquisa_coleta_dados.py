import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Simulando dados de uma pesquisa
np.random.seed(42)
dados = {
    'Pergunta_1': np.random.choice(['Sim', 'Não', 'Talvez'], size=100),      # "Você recomendaria este produto?"
    'Pergunta_2': np.random.randint(1, 5, size=100),                         # "Em uma escala de 1 a 5, como você avalia a qualidade desse produto?"
    'Grupo': np.random.choice(['Grupo A', 'Grupo B'], size=100)
}

df = pd.DataFrame(dados)

# Objetivo: Analisar as respostas do Grupo A para a Pergunta_1

# Filtro para o grupo A

df_grupo_a = df[df['Grupo'] == 'Grupo A']

# Calculando a proporção das respostas para o Grupo A

df_perc_a = df_grupo_a['Pergunta_1'].value_counts(normalize=True).mul(100).reset_index()
df_perc_a.columns = ['Pergunta_1', 'Percentual']
ordem = ['Sim', 'Não', 'Talvez']
# Visualização com Seaborn - Percentual de Pergunta 1 para o Grupo A

plt.figure(figsize=(12, 6))
sns.set_style("whitegrid")
plt.subplot(1, 2, 1)
sns.barplot(x='Pergunta_1', y='Percentual', hue='Pergunta_1', data=df_perc_a, order=ordem, hue_order=ordem, palette='viridis', dodge=False, legend=False)
plt.title('Grupo A')
plt.xlabel('Resposta Pergunta 1', fontsize=12)
plt.ylabel('Percentual (%)', fontsize=12)
plt.ylim(0, 45)

# Objetivo 2: Analisar as respostas do Grupo B para a Pergunta_1

# Filtro para o Grupo B

df_grupo_b = df[df['Grupo'] == 'Grupo B']

# Calculando a proporção das respostas para o Grupo B

df_perc_b = df_grupo_b['Pergunta_1'].value_counts(normalize=True).mul(100).reset_index()
df_perc_b.columns = ['Pergunta_1', 'Percentual']

# Visualização com Seaborn - Percentual de pergunta 1 para o Grupo B

plt.subplot(1, 2, 2)
sns.barplot(x='Pergunta_1', y='Percentual', hue='Pergunta_1', data=df_perc_b, order=ordem, hue_order=ordem, palette='viridis', dodge=False, legend=False)

# Ajuste de títulos e eixos
plt.title('Grupo B')
plt.xlabel('Resposta Pergunta 1', fontsize=12)
plt.ylabel('Percentual (%)', fontsize=12)
plt.ylim(0, 45)


plt.tight_layout()
plt.show()
