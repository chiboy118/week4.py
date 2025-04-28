def modify_text(text):
    """
    Modifies the input text.
    For this example, we'll convert the text to uppercase.
    """
    return text.upper()

# --- Main Program ---

input_filename = input("Enter the name of the file to read: ")

try:
    # Attempt to open and read the input file
    with open(input_filename, 'r') as infile:
        content = infile.read()

    # Modify the content
    modified_content = modify_text(content)

    # Define the output filename
    output_filename = "modified_" + input_filename

    # Write the modified content to a new file
    with open(output_filename, 'w') as outfile:
        outfile.write(modified_content)

    print(f"\nFile successfully modified and saved as: {output_filename}")

except FileNotFoundError:
    print("\nError: The file does not exist. Please check the filename and try again.")

except IOError:
    print("\nError: The file could not be read or written. Please check permissions or disk space.")
