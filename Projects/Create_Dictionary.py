import os # Import the 'os' module to work with file and directory operations

def generate_file_list(): # Define a function to generate a list of files and their details
      file_list = []  # Create an empty list to store file information
      for file in os.listdir():  # Iterate through the items in the current directory
             if os.path.isfile(file):  # Check if the item is a file
                file_dict = {  # Create a dictionary to store file details
                "file_name": file,                      # Store the file name
                "file_path": os.path.abspath(file),     # Get and store the absolute file path
                "file_size": os.path.getsize(file)      # Get and store the file size in bytes
            }
                file_list.append(file_dict)   # Append the file dictionary to the file list
      return file_list     # Return the list of file dictionaries


if __name__ == "__main__": # Check if the script is being run as the main program
       files = generate_file_list()  # Call the 'generate_file_list' function to get the list of files
       for file in files: # Iterate through the list of files and print their details
            print(file)