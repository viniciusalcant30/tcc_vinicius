from newspaper import Article

# Get url content - newspaper3k
def extract_url_content(url):
    article = Article(url)
    try:
        article.download()
        article.parse()
        html_content = article.html
        text = article.text
    except:
        text = 'ERROR'
    return text