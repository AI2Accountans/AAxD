import os

search_dir = r"C:\Users\IPHIX\Documents\Projects\DFRNT"
for root, dirs, files in os.walk(search_dir):
    for file in files:
        if file.endswith('.mfd'):
            print(os.path.join(root, file))
