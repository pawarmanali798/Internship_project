import os
from langchain_cohere import ChatCohere
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain.agents import initialize_agent
from langchain.agents import ZeroShotAgent
from langchain.tools import  Tool
from dotenv import load_dotenv
from serpapi import GoogleSearch

load_dotenv()

COHERE_API_KEY = os.getenv("COHERE_API_KEY")
serpapi_api_KEY = os.getenv("SERPAPI_API_KEY")

llm = ChatCohere(model="command-r", api_key=COHERE_API_KEY)

class SerpApiTool(Tool):
    def __init__(self,name,run,description):
        self.name=name
        self.func=run
        self.description=description

        name = "SerpApi"
        description = "Use this tool to search the web for information. Input is a search query. Output is a list of results."

    def run(self, query: str) -> str:
        search = GoogleSearch(api_key=serpapi_api_KEY)
        results = search.get_dict(q=query)
        return results  

    async def _arun(self, query: str) -> str:
        return await self.run(query)
    

tools = load_tools(["llm-math", SerpApiTool()], llm=llm)

agent = initialize_agent(
    tools,
    llm,
    agent=ZeroShotAgent,
    verbose=True,
)

print("Enter a query:")
query = input()
agent.run(query)