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