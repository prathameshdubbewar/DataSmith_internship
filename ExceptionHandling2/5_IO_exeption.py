try:
    filename = input("Enter the filename: ")

    with open(filename, 'r') as file:
        contents = file.read()
        print("File contents:")
        print(contents)

except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")

except IOError as e:
    print(f"Error: Cannot read the file '{filename}': {e}")
