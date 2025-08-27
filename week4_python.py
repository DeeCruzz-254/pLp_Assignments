def read_and_modify_file():
    # Ask user for input file name
    input_filename = input("Enter the name of the file to read: ")
    
    try:
        # Try opening the input file
        with open(input_filename, 'r', encoding='utf-8') as infile:
            lines = infile.readlines()
            
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
        return
    except PermissionError:
        print(f"Error: You don't have permission to read '{input_filename}'.")
        return
    except Exception as e:
        print(f"An unexpected error occurred while reading the file: {e}")
        return

    # Modify content: Add line numbers as an example
    modified_lines = [f"{i+1}: {line}" for i, line in enumerate(lines)]

    # Create output filename (e.g. input.txt → input_modified.txt)
    if '.' in input_filename:
        name_part, ext = input_filename.rsplit('.', 1)
        output_filename = f"{name_part}_modified.{ext}"
    else:
        output_filename = input_filename + "_modified"

    try:
        with open(output_filename, 'w', encoding='utf-8') as outfile:
            outfile.writelines(modified_lines)
        print(f"Modified file successfully written to '{output_filename}'.")
        
    except PermissionError:
        print(f"Error: You don't have permission to write to '{output_filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred while writing the file: {e}")


if __name__ == "__main__":
    read_and_modify_file()
