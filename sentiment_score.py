import pandas as pd 
import numpy as np
import nltk

def read_liwc(file):
    '''Leitura do dicionário LIWC para Dataframe'''
    liwc = pd.read_csv(file)

    #seleção de colunas
    liwc = liwc[['DicTerm', 'affect', 'posemo', 'negemo', 'anx', 'anger', 'sad',
                        'family', 'health', 'ingest', 'work', 'money', 'relig', 'death'
                        ]].copy()

    # criação coluna 'score' com valore 1 (+) e -1 (-)
    posemo = liwc['posemo'].values
    negemo = liwc['negemo'].values
    liwc['score_liwc2015'] = np.where(posemo == 'X', 1, 0) + np.where(negemo == 'X', -1, 0)

    cols = list(liwc.columns) # alteração da ordem das colunas 
    cols.reverse()
    liwc = liwc[cols]
    
    liwc.drop(['posemo','negemo'],axis=1, inplace=True)
    
    return liwc



def get_sentiment_score(text, dictionary):
    tokens = nltk.word_tokenize(text,language='portuguese')

    df_tokens = pd.DataFrame({'tokens':tokens})
    df_tokens['tokens'] = df_tokens['tokens'].astype('str').str.lower()

    result = pd.merge(df_tokens, dictionary, left_on='tokens',right_on='DicTerm', how='left')
    result['score_liwc2015'].fillna(0, inplace=True)

    count_n = (result['score_liwc2015'] == -1).sum()
    count_p = (result['score_liwc2015'] == 1).sum()

    result_score = result.loc[result['score_liwc2015'] != 0,'score_liwc2015'].mean()

    return f'positivo {count_p} / negativo: {count_n} / mean_score: {result_score}'