from statsmodels.tsa.stattools import adfuller, kpss

def teste_estacionariedade(series, test_type):
    if test_type == 'adf':
        teste = adfuller
        name = 'ADF'

    elif test_type == 'kpss':
        teste = kpss
        name = 'KPSS'
    else: 
        print('type not found') 
        return           

    result = teste(series)
    estat_teste = result[0]
    p_valor_teste = result[1]
    
    if p_valor_teste < 0.05:
        print(f"O valor-p do teste {name} é: {round(p_valor_teste,4)}")
        print(f"A série parece ser estacionária com base no teste {name}.")
        print(f"A estatistica de teste é {estat_teste}")
    else:
        print(f"O valor-p do teste {name} é: {round(p_valor_teste,4)}")
        print(f"A série parece ser não estacionária com base no teste {name}.")
        print(f"A estatistica de teste é {estat_teste}")

    return result