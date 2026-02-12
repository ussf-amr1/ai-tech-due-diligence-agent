import os

def analyze_project(project_path):
    """
    Analyze project files and count file types.
    Returns a dictionary like {'py': 2, 'js': 1, 'md': 1}
    """
    file_count = {}
    for root, dirs, files in os.walk(project_path):
        for file in files:
            ext = file.split('.')[-1]
            file_count[ext] = file_count.get(ext, 0) + 1
    return file_count