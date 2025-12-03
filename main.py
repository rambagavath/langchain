import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate


load_dotenv()


def main():
    template = 'give me a poem about {focus_item}'
    ptemplate = PromptTemplate(input_variables='focus_item', template=template)
    # llm = ChatOpenAI(temperature=0.7, model="gpt-5")
    llm = ChatOllama(temperature=0.7, model="gemma3:1b")
    chain = ptemplate | llm
    response = chain.invoke(input={'focus_item': 'laptop'})
    print(response.content)




if __name__ == "__main__":
    main()
