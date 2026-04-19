import os
from langchain_openai import ChatOpenAI

def handle_user_request(request_data):
    """
    CANARY TEST: This file is intentionally vulnerable to test RepoGuard.
    VULNERABILITY 1: Command Injection via shell=True
    """
    cmd = request_data.get('command', 'ls')
    # CRITICAL: Intentional Command Injection for scanner verification
    os.system(f"echo 'Executing: {cmd}' && {cmd}")

    """
    VULNERABILITY 2: Prompt Injection via .format()
    """
    user_input = request_data.get('input', '')
    prompt_template = "Translate the following to French: {user_text}"
    
    # HIGH: Intentional Prompt Injection for scanner verification
    formatted_prompt = prompt_template.format(user_text=user_input)
    
    llm = ChatOpenAI(model="gpt-4o")
    return llm.invoke(formatted_prompt)

if __name__ == "__main__":
    test_req = {'command': 'whoami', 'input': 'Hello world'}
    handle_user_request(test_req)
