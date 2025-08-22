# File Handling & Exception Handling Assignment

# Step 1: Create and write to a file
with open("original.txt", "w") as f:
    f.write("Yooh broh, this is the gaff!\n")
    f.write("Python file handling is smooth.\n")
    f.write("Music is therapy indeed!\n")

print("✅ File 'original.txt' created and written successfully.\n")

# Step 2: Ask user for filename and handle errors
filename = input("Enter the filename to read: ")

try:
    with open(filename, "r") as f:
        content = f.read()
        print("\n📂 Content of the file:")
        print(content)

    # Step 3: Modify the content and write into a new file
    modified_content = content.upper()   # simple modification: make all text uppercase

    with open("modified.txt", "w") as f:
        f.write(modified_content)

    print("\n✅ Modified content written to 'modified.txt' successfully!")

except FileNotFoundError:
    print(f"❌ Error: The file '{filename}' was not found.")
except IOError:
    print(f"❌ Error: Could not read the file '{filename}'.")
