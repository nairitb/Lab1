import os
from string import digits
import time

def rename_files():
    file_names = os.listdir(r"F:\NAIRIT\PyCharm\EICT\Lab1\prank")
    print(file_names)
    current_working_directory = os.getcwd()
    print(current_working_directory)
    os.chdir(r"F:\NAIRIT\PyCharm\EICT\Lab1\prank")
    current_working_directory = os.getcwd()
    print(current_working_directory)
    for filename in file_names:
        os.rename(filename, filename.translate(str.maketrans('', '', digits)))


rename_files()