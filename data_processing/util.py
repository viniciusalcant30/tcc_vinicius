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

    first = 'Company: '
    second = 'Ticket: '

    substituicoes = {
        "PETR4":                             f"{first}Petrobras | {second}PETR4",
        "Petrobras":                         f"{first}Petrobras | {second}PETR4",
        "PETROLEO BRASILEIRO S A PETROBRAS": f"{first}Petrobras | {second}PETR4",
        "VALE3":                             f"{first}Vale | {second}VALE3",
        "Vale":                              f"{first}Vale | {second}VALE3",
        "VALE S.A.":                         f"{first}Vale | {second}VALE3",
        "ITUB4":                             f"{first}Itaú Unibanco | {second}ITUB4",
        "Itaú Unibanco":                     f"{first}Itaú Unibanco | {second}ITUB4",
        "ITAU UNIBANCO HOLDING S.A.":        f"{first}Itaú Unibanco | {second}ITUB4",
        "ABEV3":                             f"{first}Ambev | {second}ABEV3",
        "Ambev":                             f"{first}Ambev | {second}ABEV3",
        "AMBEV S.A.":                        f"{first}Ambev | {second}ABEV3",
        "WEGE3":                             f"{first}WEG | {second}WEGE3",
        "WEG":                               f"{first}WEG | {second}WEGE3",
        "WEG SA":                            f"{first}WEG | {second}WEGE3",
        "BBDC4":                             f"{first}Banco Bradesco | {second}BBDC4",
        "Banco Bradesco":                    f"{first}Banco Bradesco | {second}BBDC4",
        "BANCO BRADESCO S.A.":               f"{first}Banco Bradesco | {second}BBDC4",
        "BBAS3":                             f"{first}Banco do Brasil | {second}BBAS3",
        "Banco do Brasil":                   f"{first}Banco do Brasil | {second}BBAS3",
        "BANCO DO BRASIL SA":                f"{first}Banco do Brasil | {second}BBAS3",
        "BPAC11":                            f"{first}Banco BTG Pactual | {second}BPAC11",
        "Banco BTG Pactual":                 f"{first}Banco BTG Pactual | {second}BPAC11",
        "BANCO BTG PACTUAL S.A.":            f"{first}Banco BTG Pactual | {second}BPAC11",
        "SANB3":                             f"{first}Banco Santander | {second}SANB3",
        "Banco Santander":                   f"{first}Banco Santander | {second}SANB3",
        "BANCO SANTANDER (BRASIL) S.A.":     f"{first}Banco Santander | {second}SANB3",
        "ITSA4":                             f"{first}Itaúsa | {second}ITSA4",
        "Itaúsa":                            f"{first}Itaúsa | {second}ITSA4",
        "ITAUSA S.A.":                       f"{first}Itaúsa | {second}ITSA4"
}

    
    df_col = df_col.copy() 

    return df_col.map(substituicoes)