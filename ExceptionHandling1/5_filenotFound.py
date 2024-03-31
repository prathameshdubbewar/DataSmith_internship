try:

    file_name = input("Enter the file name: ")
    
    with open(file_name, 'r') as file:
        contents = file.read()
        print("file Contents:")
        print(contents)
        
except FileNotFoundError:
    print(f"Error: File '{file_name}' not found.")
