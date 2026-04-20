import os

def list_files(directory):
    # INTENTIONAL COMMAND INJECTION RISK
    os.system("ls " + directory)

def safe_calc(a, b):
    # Safe code
    return a + b
