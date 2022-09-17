import pandas
import sys
print(sys.builtin_module_names)
import time
print(dir(time))
import os
print(sys.prefix)
print(os.path.exists("../Functions/vegetables.txt"))

# while True:
#     if os.path.exists("../Functions/vegetables.txt"):
#         with open("../Functions/vegetables.txt", "w+") as f:
#             print(f.read())
#     else:
#         print("File does not exist.")
#     time.sleep(5)

while True:
    if os.path.exists("SampleCSVFile_11kb.csv"):
        data = pandas.read_csv("SampleCSVFile_11kb.csv")
        print(data.mean())
    else:
        print("File does not exist.")
    time.sleep(5)