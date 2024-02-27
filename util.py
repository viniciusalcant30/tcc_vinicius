import pandas as pd
import os


def get_dataframe(local_path):
    '''
    Leitura da paste onde está baixado os arquivos e transformação dos arquivos 
    .parquet em um único dataframe
    
    '''

    file_list = os.listdir(local_path)

    dataframes = []
    for file in file_list: 
        file_path = os.path.join(local_path,file)
        df = pd.read_parquet(file_path)
        dataframes.append(df)

    result = pd.concat(dataframes)
    return result.reset_index(drop=True)


def substituir_nomes(df_col):
    """padronização das chaves para verificar se uma notícia é relevante ou não"""

    first = 'Ticket: '
    second = 'company name: '
    substituicoes = {
        "PETR4": f"{first}PETR4 - {second}Petrobras",
        "Petrobras": f"{first}PETR4 - {second}Petrobras",
        "PETROLEO BRASILEIRO S A PETROBRAS": f"{first}PETR4 - {second}Petrobras",
        "VALE3": f"{first}VALE3 - {second}Vale",
        "Vale": f"{first}VALE3 - {second}Vale",
        "VALE S.A.": f"{first}VALE3 - {second}Vale",
        "ITUB4": f"{first}ITUB4 - {second}Itaú Unibanco",
        "Itaú Unibanco": f"{first}ITUB4 - {second}Itaú Unibanco",
        "ITAU UNIBANCO HOLDING S.A.": f"{first}ITUB4 - {second}Itaú Unibanco",
        "ABEV3": f"{first}ABEV3 - {second}Ambev",
        "Ambev": f"{first}ABEV3 - {second}Ambev",
        "AMBEV S.A.": f"{first}ABEV3 - {second}Ambev",
        "WEGE3": f"{first}WEGE3 - {second}WEG",
        "WEG": f"{first}WEGE3 - {second}WEG",
        "WEG SA": f"{first}WEGE3 - {second}WEG",
        "BBDC4": f"{first}BBDC4 - {second}Banco Bradesco",
        "Banco Bradesco": f"{first}BBDC4 - {second}Banco Bradesco",
        "BANCO BRADESCO S.A.": f"{first}BBDC4 - {second}Banco Bradesco",
        "BBAS3": f"{first}BBAS3 - {second}Banco do Brasil",
        "Banco do Brasil": f"{first}BBAS3 - {second}Banco do Brasil",
        "BANCO DO BRASIL SA": f"{first}BBAS3 - {second}Banco do Brasil",
        "BPAC11": f"{first}BPAC11 - {second}Banco BTG Pactual",
        "Banco BTG Pactual": f"{first}BPAC11 - {second}Banco BTG Pactual",
        "BANCO BTG PACTUAL S.A.": f"{first}BPAC11 - {second}Banco BTG Pactual",
        "SANB3": f"{first}SANB3 - {second}Banco Santander",
        "Banco Santander": f"{first}SANB3 - {second}Banco Santander",
        "BANCO SANTANDER (BRASIL) S.A.": f"{first}SANB3 - {second}Banco Santander",
        "ITSA4": f"{first}ITSA4 - {second}Itaúsa",
        "Itaúsa": f"{first}ITSA4 - {second}Itaúsa",
        "ITAUSA S.A.": f"{first}ITSA4 - {second}Itaúsa"
    }
    
    df_col = df_col.copy() 

    return df_col.map(substituicoes)