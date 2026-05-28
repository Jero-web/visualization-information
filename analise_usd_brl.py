import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configurações de estilo
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

def carregar_dados(caminho):
    df = pd.read_csv(caminho)
    df['Data'] = pd.to_datetime(df['Data'], format='%d.%m.%Y')
    df = df.sort_values('Data')
    return df

def gerar_graficos(df):
    # 1. Gráfico de Linha: Evolução Temporal (Série Temporal)
    plt.figure(figsize=(12, 6))
    plt.plot(df['Data'], df['USD_BRL'], color='blue', linewidth=1)
    plt.title('Evolução da Taxa de Câmbio USD/BRL ao Longo do Tempo', fontsize=14)
    plt.xlabel('Ano', fontsize=12)
    plt.ylabel('Preço (BRL)', fontsize=12)
    plt.savefig('grafico_linha_evolucao.png')
    plt.close()

    # 2. Histograma: Distribuição de Frequência dos Preços
    plt.figure(figsize=(12, 6))
    sns.histplot(df['USD_BRL'], bins=30, kde=True, color='green')
    plt.title('Distribuição de Frequência do Preço USD/BRL', fontsize=14)
    plt.xlabel('Preço (BRL)', fontsize=12)
    plt.ylabel('Frequência', fontsize=12)
    plt.savefig('grafico_histograma_distribuicao.png')
    plt.close()

    # 3. Boxplot: Variação por Ano (Unidade de Tempo Agrupada)
    df['Ano'] = df['Data'].dt.year
    plt.figure(figsize=(12, 6))
    sns.boxplot(x='Ano', y='USD_BRL', data=df, palette='viridis')
    plt.title('Variação Anual do USD/BRL (Boxplot)', fontsize=14)
    plt.xlabel('Ano', fontsize=12)
    plt.ylabel('Preço (BRL)', fontsize=12)
    plt.savefig('grafico_boxplot_anual.png')
    plt.close()

if __name__ == "__main__":
    caminho_arquivo = 'USD_BRL_hist.csv'
    try:
        df_usd = carregar_dados(caminho_arquivo)
        gerar_graficos(df_usd)
        print("Gráficos gerados com sucesso!")
        
        # Estatísticas básicas para o relatório
        stats = df_usd['USD_BRL'].describe()
        print("\nEstatísticas do USD/BRL:")
        print(stats)
    except Exception as e:
        print(f"Erro ao processar os dados: {e}")
