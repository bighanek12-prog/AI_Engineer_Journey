


#Reading operation on file

with open("students.txt", "r") as file:
    print(file.read())


# Writing operation on file

with open("students.txt", "w") as file:
    file.write("Kunal\n")


# Append

with open("students.txt", "a") as file:
    file.write("Rahul\n")

    # Exception Handling using try /except 
# try:
#     with open("students.txt", "r") as file:
#         print(file.read())
# except FileNotFoundError:
#     print("File not found!")
# try:
#     with open("abc.txt", "r") as file:
#         print(file.read())
# except FileNotFoundError:
#     print("File not found!")