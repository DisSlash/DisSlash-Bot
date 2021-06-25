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
                    final_path_file = "cogs." + folder + "." + file_name[:-3]
                    cogs.append(final_path_file)
                else:
                    pass
    return cogs

list_of_cogs = list_ext()
