from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import openai
import os
from dotenv import load_dotenv
import phi
from phi.playground import Playground ,serve_playground_app
phi.api=os.getenv("API_KEY")
load_dotenv()
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
app=Playground(agents=[web_search_agent,financial_agent]).get_app()
if __name__ == "__main__":
    serve_playground_app("playground:app",reload=True)
