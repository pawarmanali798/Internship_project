import os
from langchain_cohere import ChatCohere
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain.agents import create_react_agent  
from langchain.agents import ZeroShotAgent # Import the base agent class
from langchain_community.utilities import GoogleSearchAPIWrapper
from langchain_core.tools import Tool 
from dotenv import load_dotenv
# from serpapi import GoogleSearch

load_dotenv()

COHERE_API_KEY = os.getenv("COHERE_API_KEY")
serpapi_api_KEY = os.getenv("SERPAPI_API_KEY")

llm = ChatCohere(model="command-r", api_key=COHERE_API_KEY)

search = GoogleSearchAPIWrapper()

tool = Tool(
    name="google_search",
    description="Search Google for recent results.",
    func=search.run,
)

agent = create_react_agent(
    llm=llm, 
    tools=[tool], 
    agent_type=ZeroShotReactDescriptionAgent, 
    verbose=True
)

print("Enter a query:")
query = input()
agent.run(query)