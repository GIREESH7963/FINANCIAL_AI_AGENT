from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import openai
import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key=os.getenv("OPENAI_API_KEY")
#WEBSEARCH AGENT
web_search_agent=Agent(
    name="Web Search Agent",
    role="search the web for information",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tools_calls=True,
    markdown=True)
##financial agent
financial_agent=Agent(
    name="Financial Agent",
    role="get financial information",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True)],
    instructions=["Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)
multi_ai_agent=Agent(
    name="Multi AI Agent",
    role="get information from multiple sources",
    team=[web_search_agent,financial_agent],
    instructions=["Always include sources","Use tables to display data"],
    show_tools_calls=True,
    markdown=True,
    model=Groq(id="llama-3.1-70b-versatile")
)
multi_ai_agent.print_response("Summarize analyst recommendation and share the latest news for Nvidia",stream=True)

    
