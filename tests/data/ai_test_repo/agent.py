from langchain.agents import initialize_agent, Tool
from langchain_community.tools import ShellTool
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(temperature=0)
shell_tool = ShellTool()

# UNSAFE TOOL USAGE: Agent has access to shell and is exposed to user prompts
agent = initialize_agent(
    [shell_tool], 
    llm, 
    agent="zero-shot-react-description", 
    verbose=True
)

def run_agent(user_prompt):
    return agent.run(user_prompt)
