
# Imports

from shutil import copyfile
import zipfile
from datetime import date, datetime
import os

ZipFile = zipfile.ZipFile
now = datetime.now()
time = now.strftime("%H-%M-%S")

"""
========
Code
========
"""
try:
    copyfile("./ironman.sav", f"./ironman_backup_{date.today()}_{time}.sav")
except Exception as e:
    print(e)


try:
    with ZipFile("ironman.sav", "r") as ZipFolder:
        for x in ZipFolder.namelist():
            print(x)

except Exception as e:
    print(e)

""" 
try:
    pass
except Exception as e:
    print(e)
"""