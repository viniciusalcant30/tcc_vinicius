from datetime import date
import yfinance as yf

class Stocks:
    def __init__(self, ticket) -> None:
        self.ticket =  ticket

    # busca o preço histórico em um intervalo de tempo e retorna como dataframe
    def get_price_historic(self, start_date:date, end_date:date):
        try:
            stock_data = yf.download(f'{self.ticket}.SA', start=start_date, end=end_date)
            stock_data.columns = [x.lower() for x in stock_data] # transforma as colunas em minusculo
            stock_data['price_variation'] = stock_data['close'].pct_change() * 100 # definição do preço percentual
            self.price = stock_data
            # return stock_data
        except Exception as e:
            print("Error fetching stock data:", e)
            return None
    
    # plota o grafico no intervalo de tempo dos dados
    def plot_price(self, ax):
        y = self.price['adj close']
        x = self.price.index

        x_ajusted = [j.strftime("%d/%m") for j in list(x)]

        ax.set_xticks(x)
        ax.set_xticklabels(labels=x_ajusted, rotation=45, ha='right', fontsize=9.5)

        result_plot = ax.plot(x,y, label=f'adj close price: {self.ticket}')

        return result_plot

    # plota o grágico da variação do tempo no intervalo de tempo
    def plot_pct_change(self, ax):
        y = self.price['price_variation']
        x = self.price.index

        x_ajusted = [j.strftime("%d/%m") for j in list(x)]

        ax.set_xticks(x)
        ax.set_xticklabels(labels=x_ajusted, rotation=45, ha='right', fontsize=9.5)

        result_plot = ax.plot(x,y, label=f'pct change: {self.ticket}')

        return result_plot