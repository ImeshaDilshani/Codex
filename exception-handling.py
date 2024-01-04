# Define the filename to work with
filename = "my_file.txt"

try:
    # Attempt to open the file in read mode
    with open(filename, "r") as file:
        # Read the file contents if successful
        contents = file.read()
        print("File contents:", contents)

except FileNotFoundError:
    # Handle the file not found error
    print("Error: The file", filename, "was not found.")

except PermissionError:
    # Handle permission errors
    print("Error: You do not have permission to read the file", filename)

except Exception as e:  # Catch any other unexpected errors
    print("An error occurred:", e)

else:
    # Execute if no exceptions occur
    print("File reading completed successfully!")

finally:
    # This block always executes, regardless of exceptions
    print("This code always runs, even if there were errors.")
