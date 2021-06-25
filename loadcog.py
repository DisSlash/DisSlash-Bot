import os
import glob

def list_ext():
    cogs = []
    for folder in os.listdir("./cogs"):
        for file_name in os.listdir("./cogs/" + folder):
            if file_name == "__pycache__":
                pass
            else:
                if file_name.endswith(".py"):
                    cogs.append(file_name[:-3])
                else:
                    pass
    return cogs

list_of_cogs = list_ext()
print(list_of_cogs)