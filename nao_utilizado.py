# calculo da relevanvcia:



# from langchain_openai import OpenAI
# from langchain.chains import LLMChain
# from langchain.prompts import PromptTemplate
# import os
# from dotenv import load_dotenv

# load_dotenv()





# def get_chain(OPENAI_API_KEY, template): 
    
#     prompt = PromptTemplate.from_template(template) 

#     llm = OpenAI(openai_api_key=OPENAI_API_KEY, model_name="gpt-3.5-turbo-instruct", temperature=0)

#     llm_chain = LLMChain(prompt=prompt, llm=llm)

#     return llm_chain

# def classify_relevance(texto, empresa, llm_chain):
#     result = llm_chain.run({'texto':texto, 'empresa':empresa})
    
#     # transforma em maiusculo
#     result = result.upper()

#     # remover espaços
#     result = result.replace('\n','')
    
#     # Separa o texto
#     final_result = result.split("] ", 1)
    
#     # Adiciona ']' de volta ao primeiro elemento da lista
#     final_result[0] = final_result[0] + "]"

#     return final_result


# OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

# template = """ Você é um excelente jornalista. 
#     A partir do texto: {texto}, me retorne:'[SIM]', caso o texto seja relacionado e relevante a empresa: {empresa}, ou retorne:'[NÃO]'. 
#     Sempre justifique sua resposta
#     """

# llm_chain = get_chain(OPENAI_API_KEY, template)

# result = classify_relevance(texto, empresa, llm_chain)

# teste = df.sample(20, random_state=13).copy()

# teste['classificação'] = teste.apply(lambda x: classify_relevance(x['full_text'], x['key'], llm_chain), axis=1)

# teste.to_excel('teste_classificação.xlsx')