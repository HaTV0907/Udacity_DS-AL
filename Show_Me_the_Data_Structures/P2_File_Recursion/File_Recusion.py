import os
from pathlib import Path

def find_files(directory, extension):
    files = []
    # check invalid directory
    if None == directory or "" == directory:
        print ("Invalid input path: None")
        return
    # check invalid exension
    if None == extension or "" == extension:
        print("invalid extension")
        return
    # check directory exist
    directory_path = Path(directory)
    if not directory_path.exists():
        print("directory path does not exist")
        return
    for filename in os.listdir(directory):
        path = os.path.join(directory, filename)
        if os.path.isfile(path) and filename.endswith(extension):
            files.append(path)
        elif os.path.isdir(path):
            files.extend(find_files(path, extension))
    return files

# Example usage
directory = "./testdir"
extension = ".c"
result = find_files(directory, extension)
print(result)
# null directory
directory = None
extension = ".c"
result = find_files(directory, extension)
print(result)
# empty extension
directory = "./testdir"
extension = ""
result = find_files(directory, extension)
print(result)
# not exist file extension
directory = "./testdir"
extension = ".py"
result = find_files(directory, extension)
print(result)