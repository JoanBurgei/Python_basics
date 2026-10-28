#functions methods
# print("Hello World") #built-in functions
from custom_functions import greet
with open("temp.txt", "w") as file:# it writes into a file "w" and are inbuild functions
    file.write("99.34\n")
    file.write("100\n")
    file.write("54.35\n")

with open("temp.txt", "r") as file:
    content=file.read()
    print(content)
    # pip install yt - dlp
greet()