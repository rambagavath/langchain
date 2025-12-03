import os

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from tavily import TavilyClient
load_dotenv()
from langchain_tavily import TavilySearch

# tavily = TavilyClient()
#
# @tool
# def search(query: str) -> str:
#     """
#     Tool that searches the internet
#     :param query: The query to search for
#     :return: the result of search
#     """
#     print(f'searching for query {query}')
#     return tavily.search(query)

def main():
    llm = ChatOpenAI(model='gpt-5')
    tools = [TavilySearch()]
    agent = create_agent(model=llm, tools=tools)
    result = agent.invoke(
            {
                "messages": HumanMessage(
                    content="search for 3 job postings for an ai engineer using langchain in the bay area on linkedin and list their details?"
                      # content="what's the weather in tokyo"
                )
            }
        )
    print(result)


if __name__ == "__main__":
    main()
