import datetime
import logging
import azure.functions as func
import pandas as pd
from datetime import datetime 
import bing_search as bing
import util
from pyarrow import parquet as pq
import tempfile
import os
import pytz

app = func.FunctionApp()

def process_search(searches, result_count, period="Day"):
    dfs = []
    today = datetime.now(utc_minus_3).strftime('%Y-%m-%d')
    for search_term in searches:
        result = bing.search_news(search_term, result_count, period)
        result['full_text'] = result['url'].apply(util.extract_url_content)
        result['key'] = search_term
        result['data_de_busca'] = today
        dfs.append(result)
        
    dfs_result = pd.concat(dfs) 

    return dfs_result

utc_minus_3 = pytz.timezone('Etc/GMT+3')

today = datetime.now(utc_minus_3).strftime('%Y-%m-%d-%Hh-%Mmin')
name = f'result_{today}.parquet'


@app.function_name(name="myTimer")
@app.schedule(schedule="0 0 12 * * *", arg_name="myTimer", run_on_startup=True,
              use_monitor=True) # , TimeZoneInfoId = "America/Sao_Paulo" 
@app.blob_output(arg_name="outputblob",
                path=f"result-function-stocknews/{name}",
                connection="")
def timer_trigger(myTimer: func.TimerRequest, outputblob: func.Out[bytes]) -> None:
    if myTimer.past_due:
        logging.info('The timer is past due!')

    logging.info('função iniciada!')

    searches = ['ITUB4', 'BBDC4', 'VALE3', 'MGLU3']
    
    df_result = process_search(searches,5)
    logging.info(df_result)

    # Salvar o DataFrame modificado para um arquivo Parquet temporário
    with tempfile.NamedTemporaryFile(suffix=".parquet", delete=False) as temp_file:
        df_result.to_parquet(temp_file.name, index=False)
        temp_file_path = temp_file.name

    # Ler o arquivo Parquet temporário
    with open(temp_file.name, 'rb') as temp_file_read:
        parquet_content = temp_file_read.read()

    # Definir o outputblob como o conteúdo do arquivo Parquet
    outputblob.set(parquet_content)

    # Remover o arquivo Parquet temporário
    temp_file.close()
    
    try:
        os.remove(temp_file_path)
        logging.info(f"Arquivo temporário em {temp_file_path} excluído com sucesso.")
    except FileNotFoundError:
        logging.warning(f"O arquivo temporário em {temp_file_path} não foi encontrado.")
    except Exception as e:
        logging.error(f"Erro ao excluir o arquivo temporário: {str(e)}")

    logging.info('Python timer trigger function executed.')