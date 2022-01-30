import os
import datetime
import shutil

path = input("path to clear files and folders")
days = int(input("give number o days limit"))

exist = os.path.exists(path)

if(exist == False):
    print("please provide the valid path")
    path = input("give a path to clear files and folders")

    if(os.path.isfile(path)):
        print("please provide path of a directory")
        path = input("give a path to clear files and folders")


    for root, dirs, files in os.walk(path, topdown = False):
        for file in files:
            full_path = os.path.join(root, file)
            presentTime = datetime.datetime.now()
            file_cre_time = datetime.datetime.fromtimestamp(os.path.getctime(full_path))
            number_of_days = (presentTime - file_cre_time).days

            if (number_of_days >=days):
                os.remove(full_path)
                print("congratulations, your pc is clean ")

            for i in dirs:
                folder_path = os.path.join(root, i)
                if len(os.listdir(folder_path))== 0:
                    shutil.rmtree(folder_path)
                    print("congratulations, your pc is clean ")












