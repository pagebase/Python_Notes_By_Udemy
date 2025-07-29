import os

fp=open("Log.md","w")

# Basic directory walk
for root, dirs, files in os.walk('D:\\'):
    for file in files:
        print(os.path.join(root, file))  # Prints full path to each file
        fp.write(f"# {os.path.join(root,file)}\n")
