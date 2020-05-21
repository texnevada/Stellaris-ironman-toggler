# Imports
from shutil import copyfile
import zipfile
from datetime import date, datetime
import os

"""
=======
Prep
=======
"""

ZipFile = zipfile.ZipFile
now = datetime.now()
timenow = now.strftime(f"%H-%M-%S-%f")

"""
========
Code
========
"""


def backup():
    try:
        print("[INFO]: Backing up your save.")
        copyfile("./ironman.sav", f"./ironman_backup_{date.today()}_{timenow}.sav")
        print("[INFO]: Backup complete.")
        extraction()
    except Exception as e:
        print(f"[WARN]: {e}")


def extraction():
    try:
        with ZipFile("ironman.sav", "r") as zipf:
            zipf.extractall()
            zipf.close()
        os.remove("ironman.sav")
        print("[INFO]: Extracted files from save")
        save_edit()
    except Exception as e:
        print(f"[WARN]: {e}")


def save_edit():
    try:
        print("[INFO]: Reading meta file & preparing changes")
        file = open("meta", "r")
        open("meta_new", "x")
        file2 = open("meta_new", "a")
        for line in file:
            if "ironman=yes" in line:
                print("[INFO]: Found ironman reference.")
                print("[INFO]: Disabling ironman")
                file2.write("ironman=no")
                print("[INFO]: Finishing up meta changes")
            elif "ironman=no" in line:
                print("[INFO]: Found ironman reference.")
                print("[INFO]: Enabling ironman")
                file2.write("ironman=yes")
                print("[INFO]: Finishing up meta changes")
            else:
                file2.write(line)
        file.close()
        file2.close()
        print("[INFO]: Finished the new meta file")

        print("[INFO]: Reading gamestate file & preparing changes")
        file = open("gamestate", "r")
        open("gamestate_new", "x")
        file2 = open("gamestate_new", "a")
        for line in file:
            if "ironman=yes" in line:
                print("[INFO]: Found ironman reference.")
                print("[INFO]: Disabling ironman")
                file2.write("	ironman=no\n")
            elif "ironman=no" in line:
                print("[INFO]: Found ironman reference.")
                print("[INFO]: Enabling ironman")
                file2.write("	ironman=yes\n")
            else:
                file2.write(line)
        file.close()
        file2.close()
        print("[INFO]: Finished the new gamestate file")

        os.remove("meta")
        os.rename("meta_new", "meta")

        os.remove("gamestate")
        os.rename("gamestate_new", "gamestate")
        insertion()
    except Exception as e:
        print(f"[WARN]: {e}")


def insertion():
    try:
        with ZipFile("ironman.sav", "a") as ZipFolder:
            print("[INFO]: Adding new meta file to ironman save")
            ZipFolder.write("meta")
            print("[INFO]: Adding new gamestate file to ironman save")
            ZipFolder.write("gamestate")
            ZipFolder.close()
        os.remove("meta")
        os.remove("gamestate")
        input("[INFO]: DONE. PRESS ENTER TO EXIT PROGRAM")
    except Exception as e:
        print(f"[WARN]: {e}")


backup()
