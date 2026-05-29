import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- CONFIGURAÇÕES INICIAIS ---
# Defini o tema visual como sugerido nas unidades.
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

def carregar_dados(caminho):
    """
    Carrega o dataset real de USD/BRL e prepara as datas.
    """
    df = pd.read_csv(caminho)
    df['Data'] = pd.to_datetime(df['Data'], format='%d.%m.%Y')
    df = df.sort_values('Data')
    return df

def gerar_graficos(df):
    """
    Gera três gráficos baseados em conceitos de visualização de diferentes unidades de ensino.
    """
    
    # --- 1. GRÁFICO DE LINHA (Série Temporal) ---
    # Unidade: Visualização de Dados Temporais.
    # Mostra a evolução do preço do dólar ao longo dos anos.
    plt.figure(figsize=(12, 6))
    plt.plot(df['Data'], df['USD_BRL'], color='blue', linewidth=1)
    plt.title('Evolução da Taxa de Câmbio USD/BRL (Série Temporal)', fontsize=14)
    plt.xlabel('Ano', fontsize=12)
    plt.ylabel('Preço (BRL)', fontsize=12)
    plt.savefig('grafico_linha_evolucao.png')
    plt.close()

    # --- 2. HISTOGRAMA (Distribuição) ---
    # Unidade: Conceitos de Distribuição e Frequência.
    # Mostra a concentração dos valores de câmbio no período.
    plt.figure(figsize=(12, 6))
    sns.histplot(df['USD_BRL'], bins=30, kde=True, color='green')
    plt.title('Distribuição de Frequência do Preço USD/BRL', fontsize=14)
    plt.xlabel('Preço (BRL)', fontsize=12)
    plt.ylabel('Frequência', fontsize=12)
    plt.savefig('grafico_histograma_distribuicao.png')
    plt.close()

    # --- 3. GRÁFICO DE BARRAS (Comparação de Médias Anuais) ---
    # Unidade: Visualização de Variáveis Categóricas vs Numéricas.
    # Mostra a média do dólar para cada ano, facilitando a comparação direta.
    df['Ano'] = df['Data'].dt.year
    media_anual = df.groupby('Ano')['USD_BRL'].mean().reset_index()
    
    plt.figure(figsize=(12, 6))
    sns.barplot(x='Ano', y='USD_BRL', data=media_anual, palette='viridis')
    plt.title('Média Anual da Taxa de Câmbio USD/BRL', fontsize=14)
    plt.xlabel('Ano', fontsize=12)
    plt.ylabel('Preço Médio (BRL)', fontsize=12)
    plt.savefig('grafico_barras_media_anual.png')
    plt.close()

if __name__ == "__main__":
    caminho_arquivo = 'USD_BRL_hist.csv'
    try:
        df_usd = carregar_dados(caminho_arquivo)
        gerar_graficos(df_usd)
        print("Gráficos gerados com sucesso seguindo as unidades de ensino!")
        
        # Estatísticas para o relatório
        print("\nEstatísticas do USD/BRL:")
        print(df_usd['USD_BRL'].describe())
    except Exception as e:
        print(f"Erro ao processar os dados: {e}")