import os

from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic


load_dotenv()


llm = ChatAnthropic(
    model="claude-3-5-sonnet-20241022",
    anthropic_api_key=os.getenv("ANTHROPIC_API_KEY"),
    temperature=0
)