import os

def find_files(directory, extension):
    files = []
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