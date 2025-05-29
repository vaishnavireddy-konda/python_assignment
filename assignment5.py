with open("sample.txt", "w") as file:
    file.write("This is the first line.\n")
    file.write("This is the second line.\n")

with open("sample.txt", "a") as file:
    file.write("This is an appended line.\n")
    file.write("Another appended line.\n")


with open("sample.txt", "r") as file:
    content = file.read()
    print("File Content:\n")
    print(content)
