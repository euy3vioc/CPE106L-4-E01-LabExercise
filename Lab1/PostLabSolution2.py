def main():
    # Step 1: Prompt the user for a filename
    filename = input("Enter the name of the file: ")
    
    try:
        # Attempt to open the file
        with open(filename, 'r') as file:
            # Step 2: Read the file's contents and store each line in a list
            lines = file.readlines()
            
            # Step 3: Print the total number of lines
            print(f"The file contains {len(lines)} lines.")
            
            # Step 4: Loop until the user decides to quit (by entering 0)
            while True:
                line_number = int(input("Enter a line number to view (or 0 to quit): "))
                
                if line_number == 0:
                    break
                
                # Check if the line number is valid
                if 1 <= line_number <= len(lines):
                    # Print the line associated with the entered number
                    print(lines[line_number - 1])
                else:
                    print("Invalid line number. Please enter a number between 1 and", len(lines), "or 0 to quit.")
    
    except FileNotFoundError:
        print("The file was not found. Please check the filename and try again.")

if __name__ == "__main__":
    main()
