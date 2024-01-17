#Q1a)  a Python program using function to which will do the following: the function will create a text file with current timestamp.#

import datetime

def create_text_file_with_timestamp():
    # Get the current timestamp
    current_timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Generate a filename with the timestamp
    filename = f"file_{current_timestamp}.txt"

    with open(filename, 'w') as file:
        file.write("This is a text file created at: " + current_timestamp)

    print(f"Text file '{filename}' created successfully.")

# Call the function to create the text file
create_text_file_with_timestamp()

#Output- Text file 'file_2024-01-17_15-14-02.txt' created successfully.


#Q1b) a Python program using function to which will do the following: the file content should have the content of the current timestamp.#

import datetime

def content_timestamp():
    # Get the current timestamp
    current_timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Generate a filename with the timestamp
    filename = f"file_{current_timestamp}.txt"

    with open(filename, 'w') as file:
        file.write(current_timestamp)

    print(f"Text file '{filename}' created successfully with content: {current_timestamp}")

#Call the function
content_timestamp()

#Output- Text file 'file_2024-01-17_15-14-02.txt' created successfully with content: 2024-01-17_15-14-02


#Q2)  another Python function to read from a text file. The function will take the name of the text file and display the content of the file into the console#

def read_and_display_file_content(sample):
    try:
        with open(sample, 'r') as file:
            content = file.readlines()
            print(f"Content of the file '{sample}':")
            for line in content:
                print(line.strip())
    except FileNotFoundError:
        print(f"File '{sample}' not found.")

filename_read = "C:/Users/USER/Desktop/Sample.txt"
read_and_display_file_content(filename_read)

#Output-Content of the file 'C:/Users/USER/Desktop/Sample.txt':This is a Python class.This is a Python Automation course.









