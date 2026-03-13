file1 = input("Enter first file name: ")
file2 = input("Enter second file name: ")
output = input("Enter output file name: ")

try:
    with open(file1, "r") as f1, open(file2, "r") as f2:
        content1 = f1.read()
        content2 = f2.read()

    with open(output, "w") as out:
        out.write(content1)
        out.write("\n")
        out.write(content2)

    print("Files merged successfully.")

except FileNotFoundError:
    print("One or both files not found.")
