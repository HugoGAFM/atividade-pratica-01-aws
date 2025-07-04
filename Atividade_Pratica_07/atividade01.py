import pandas as pd

def analisar_logs_treinamento(nome_arquivo: str):
    
    try:
      
        df = pd.read_csv(nome_arquivo)

        
        if 'tempo_execucao' not in df.columns:
            print("Erro: coluna 'tempo_execucao' não encontrada no arquivo.")
            print(f"Colunas disponíveis: {list(df.columns)}")
            return

        
        media = df['tempo_execucao'].mean()
        desvio_padrao = df['tempo_execucao'].std()

        print("=== Análise de Tempo de Execução ===")
        print(f"Média: {media:.2f} segundos")
        print(f"Desvio padrão: {desvio_padrao:.2f} segundos")

    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado.")
    except Exception as e:
        print("Erro ao processar o arquivo:", e)


analisar_logs_treinamento("Logs_treinamento.csv")