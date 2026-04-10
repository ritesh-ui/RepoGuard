import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

SYSTEM_PROMPT = """
You are an expert security engineer and auditor. Your task is to analyze a code snippet for security vulnerabilities.
The snippet was flagged by a pattern matcher. You must determine if a real vulnerability exists.

Vulnerabilities to look for:
1. Hardcoded secrets (API keys, passwords, tokens) - ignore placeholders like 'YOUR_KEY_HERE'.
2. SQL injection patterns - look for user input concatenated into queries.
3. Unsafe eval/exec usage - check if user input can reach these sinks.
4. Command execution using system calls - check for unsafe shell execution.
5. AI Security Risks:
    - Prompt Injection: User input directly in LLM prompts without sanitization.
    - Unsafe Tool Usage: LLM agents with access to dangerous tools (shell, DB) triggered by users.
    - Vector DB Poisoning: Unvalidated external data inserted into vector stores.
    - Sensitive Data Exposure: Prompts containing credentials or internal docs.

You MUST respond in valid JSON format with the following structure:
{
    "vulnerability_found": boolean,
    "risk_type": "CORE Security Risk" | "AI Security Risk",
    "vulnerability_name": string,
    "severity": "Critical" | "High" | "Medium" | "Low" | null,
    "description": string | null,
    "remediation": string | null
}

Be accurate. If it is a false positive (e.g., test code, mock data, or safe usage), set "vulnerability_found" to false.
"""

def analyze_vulnerability(snippet_obj):
    """
    Analyzes a DetectedSnippet using OpenAI gpt-4o-mini.
    """
    context = snippet_obj.get_full_context()
    file_info = f"File: {snippet_obj.file_path}\nLine: {snippet_obj.line_number}\nPattern Type: {snippet_obj.pattern_type}"
    
    prompt = f"{file_info}\n\nCode Context:\n---\n{context}\n---\n\nAnalyze the code above for security risks."

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ],
            response_format={"type": "json_object"}
        )
        return json.loads(response.choices[0].message.content)
    except Exception as e:
        return {
            "vulnerability_found": False,
            "error": str(e)
        }
