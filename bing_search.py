import requests
import json
import pandas as pd
from html2text import html2text
import os
from dotenv import load_dotenv

load_dotenv()

AZURE_SUBSCRIPTION_KEY = os.environ.get('AZURE_SUBSCRIPTION_KEY')
AZURE_SUBSCRIPTION_KEY2 = os.environ.get('AZURE_SUBSCRIPTION_KEY2')
AZURE_ENDPOINT = os.environ.get('AZURE_ENDPOINT')

def format_search_result(funcao):
    def wrapper(*args, **kwargs):
        search_results = funcao(*args, **kwargs)

        # seleção de colunas
        name = [article["name"] for article in search_results["value"]]
        url = [article["url"] for article in search_results["value"]]
        provider = [article["provider"] for article in search_results["value"]]
        datePublished = [article["datePublished"] for article in search_results["value"]]
        descriptions = [article["description"] for article in search_results["value"]]
        category = []
        for article in search_results['value']:
            try:
                category_item = article["category"]
            except:
                category_item = 'Undefined'
            category.append(category_item)
        about = []
        for article in search_results['value']:
            try:
                about_item = article["category"]
            except:
                about_item = 'Undefined'
            about.append(about_item)


        # formatação como dataframe
        data = {'name':name, 'descriptions':descriptions, 'about':about, 'provider':provider,
                'url':url, 'datePublished':datePublished, 'category':category}

        df_bing_news = pd.DataFrame(data)
        df_bing_news['provider'] = df_bing_news['provider'].apply(lambda x: x[0]['name'])
        df_bing_news['descriptions_raw'] = df_bing_news['descriptions'] 
        df_bing_news['name_raw'] = df_bing_news['name']
        df_bing_news['descriptions'] = df_bing_news['descriptions'].apply(lambda x: html2text(x))
        df_bing_news['name'] = df_bing_news['name'].apply(lambda x: html2text(x))
        return df_bing_news       

    return wrapper


@format_search_result
def search_news(search_term, result_count, market='pt-BR'):

    search_url = f'{AZURE_ENDPOINT}v7.0/news/search'
    headers = {"Ocp-Apim-Subscription-Key" : AZURE_SUBSCRIPTION_KEY}
    params = {"q": search_term, "textDecorations": False, "textFormat": "HTML", "count":result_count, 
                'mkt':market,'setlang':'pt-br'}
    response = requests.get(search_url, headers=headers, params=params)
    response.raise_for_status()
    search_results = json.dumps(response.json())
    search_results = json.loads(search_results) # json -> dict
    
    return search_results


# params['freshness'] = 'Day'
# params['freshness'] = 'Week'
# params['freshness'] = 'Month'
# params['since']
# params['sortBy']	