import os
import time
import shutil
path = input("Enter the name of the folder")
number_of_days = time.time(input("Enter the number of days"))
if os.path.exists(path):
    list_of_files = os.walk(path)
    ctime = os.stat(path).st_ctime
    if ctime > number_of_days:
        os.remove(path)
else:
    print("Folder not found")