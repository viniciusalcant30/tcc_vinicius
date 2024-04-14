from langchain.chains import create_tagging_chain

# classificação da relevancia da notícia
def classify_relevance(company, input, llm):
    # time.sleep(10)  # Pausa o programa por 10 segundos

    # relevance_text = f"Let's think step by step: assess whether a given news article is directly pertinent to the Brazilian company {company}. First, identify the primary topics addressed in the news, then indicate if these topics are relevant to {company}. Return 1 if they are relevant, and 0 if they are not. Please give your best. forget all previous information received"

    relevance_text = f"""Implement the following process: ascertain the main topics touched upon in the news update's title and body. Determine if these are directly connected to the Brazilian firm {company}. Provide grounds for your verdict, and then allocate a score of 1 if the input is strictly linked to {company}, or a 0 if it is not"""
    schema = {
        "properties": {
            "relevance": {
                "type": "integer",
                "enum": [0,1],
                "description": relevance_text,
            }}, 
        "required": ["relevance"]
    }

    chain = create_tagging_chain(schema, llm)
    result = chain.invoke(input)
    return result['text']

# análise de sentimentos
def classify_sentiment_chain(llm):
    # time.sleep(2)  # Pausa o programa por 10 segundos
    schema = {
        "properties": {
            "sentiment": {"type": "string"},
            "sentiment score": {
                "type": "integer",
                "enum": [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5],
                # "description": f"As an expert in sentiment analysis, determine the polarity of the ideas from the text related to the {company}. Classify them from 5 to -5 where 5 is extremely positive, -5 is extremely negative, and 0 signifies neutrally",
                #   "description": """Given the consequential positive or negative implications for the company concerned, analyze adeptly. 
                #                     Rate this on a scale from -5 to 5 where -5 indicates extremely negative, 
                #                     5 indicates extremely positive, and 0 indicating neutral or no sentiment.
                #                      """
                "description": """Classify the polarity of the words in the sentence.""" 
            },
            # 'covered topics': {"type": "string"}
        },
        "required": [ "sentiment score"] # "sentiment", covered topics
    }

    chain = create_tagging_chain(schema, llm)
    return chain

def classify_sentiment(chain, input):
    try:
        result = chain.invoke(input)
        # print(result)
        return result['text']
    except:
        result = ''
        return result