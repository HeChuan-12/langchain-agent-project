from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv
import os

from tools.weather_tool import weather_tool
from tools.knowledge_tool import knowledge_tool
from tools.local_tool import local_tool
from memory.memory_config import memory

# 加载环境变量
load_dotenv()

# 使用 DeepSeek Chat 接口
llm = ChatOpenAI(
    model="deepseek-chat",
    openai_api_base="https://api.deepseek.com/v1",
    openai_api_key=os.getenv("DEEPSEEK_API_KEY")
)

# 集成工具
tools = [weather_tool, knowledge_tool, local_tool]

# 构建 Agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
    memory=memory
)

def run_agent(user_input):
    return agent.run(user_input)