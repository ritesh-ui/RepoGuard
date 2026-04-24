import os

SUPPORTED_EXTENSIONS = {'.py', '.js', '.ts', '.jsx', '.tsx', '.java', '.go', '.yaml', '.txt'}
IGNORE_DIRS = {
    '.git', 'node_modules', '__pycache__', 'venv', '.venv', 'env', '.env', 
    'dist', 'build', 'docs', 'test_repo', 'ai_test_repo', 'test_cases', 'examples',
    'i18n', 'public', 'tests', '__tests__', 'migrations', 'images'
}
REPOGUARD_CORE_FILES = {
    'scanner.py', 'llm_analyzer.py', 'ast_engine.py', 
    'agent_tools.py', 'file_loader.py', 'reporter.py', 'scan_repo.py'
}

def load_ignore_patterns(repo_path):
    """
    Loads ignore patterns from .repoinspectignore in the repository root.
    Returns a set of normalized relative paths to ignore.
    """
    ignore_path = os.path.join(repo_path, '.repoinspectignore')
    patterns = set()
    if os.path.exists(ignore_path):
        try:
            with open(ignore_path, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#'):
                        # Normalize to avoid platform issues
                        patterns.add(line.rstrip('/'))
        except Exception as e:
            print(f"Warning: Could not read .repoinspectignore: {e}")
    return patterns

def get_repo_files(repo_path):
    """
    Recursively find all supported files in the repository, respecting IGNORE_DIRS
    and the optional .repoinspectignore file.
    """
    user_ignores = load_ignore_patterns(repo_path)
    found_files = []
    
    for root, dirs, files in os.walk(repo_path):
        rel_root = os.path.relpath(root, repo_path)
        if rel_root == '.':
            rel_root = ''
            
        # 1. In-place modify dirs to skip hardcoded and user-defined ignored directories
        # We check if the dir name itself is ignored or if the full relative path is ignored
        dirs[:] = [
            d for d in dirs 
            if d not in IGNORE_DIRS 
            and os.path.join(rel_root, d).rstrip('/') not in user_ignores
        ]
        
        for file in files:
            # 2. Skip RepoInspect infrastructure
            if file in REPOGUARD_CORE_FILES:
                continue
            
            # 3. Skip user-ignored files
            rel_file_path = os.path.join(rel_root, file)
            if rel_file_path in user_ignores:
                continue
                
            # 4. Check extension
            ext = os.path.splitext(file)[1].lower()
            if ext in SUPPORTED_EXTENSIONS:
                found_files.append(os.path.join(root, file))
    
    return found_files

def read_file_content(file_path):
    """
    Read file content safely handling encoding issues.
    """
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            return f.readlines()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return []
