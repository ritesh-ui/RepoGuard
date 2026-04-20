import openai
from langchain.prompts import PromptTemplate

def get_answer(user_input):
    template = "You are a helpful assistant. Answer the following question: {question}"
    # PROMPT INJECTION RISK: User input directly formatted into template
    prompt = template.format(question=user_input)
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
