from GoogleNews import GoogleNews 
import pandas as pd

def search_news(search_term, page_count,period=False, start_date='02/28/2020', end_date=False):
    googlenews = GoogleNews(lang='pt', region='BR')

    if period:
        googlenews.set_period(period)

    if start_date and end_date:
        googlenews.set_time_range(start_date, end_date)

    googlenews.search(search_term)
    
    if page_count == 1:
        result = googlenews.results()
    else:    
        page_count+=1
        for i in range(2,page_count):   
            googlenews.getpage(i)
            result=googlenews.result()
            
    df_gnews=pd.DataFrame(result)    
    # df_gnews['link'] = df_gnews['link'].apply(lambda x: x.split('&ved=')[0])
    return df_gnews