import os
path = 'C:/Users/imeke/Desktop/PP2_2025_LABS/labs'


directories = []
files = []

for item in os.listdir(path):
    full_path = os.path.join(path, item)
    
    if os.path.isdir(full_path):
        directories.append(item)
    elif os.path.isfile(full_path):
        files.append(item)
        
print(files)
print(directories)
