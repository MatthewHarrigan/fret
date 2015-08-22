import os
def list_files(dir_path, first_file):
    files = os.listdir(dir_path)
    start = files.index(first_file)
    return files[start:]
    
