try:
    file_name = input("Enter the filename: ")
    with open(file_name, 'r') as file:
        contents = file.read()
    print("File contents:")
    print(contents)
except PermissionError:
    print("Error: No Permission to access")
except FileNotFoundError:
    print("Error: File not found")
