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

# Visualização com Seaborn - Percentual de Pergunta 1 para o Grupo A

plt.figure(figsize=(8, 6))
sns.set_style("whitegrid")
sns.barplot(x='Pergunta_1', y='Percentual', hue='Pergunta_1', data=df_perc_a, palette='viridis', dodge=False, legend=False)

# Ajuste de títulos e eixos
plt.title('Percentual de Repostas Pergunta 1 - Grupo A', fontsize=16)
plt.xlabel('Resposta Pergunta 1', fontsize=12)
plt.ylabel('Percentual (%)', fontsize=12)
plt.tight_layout()
plt.show()