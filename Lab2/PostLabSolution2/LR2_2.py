namefile = input("Enter the File text name (include .txt): ")
with open(namefile, "r") as text:
    text_lines = text.readlines()
num_lines = len(text_lines)
print("The file has {} lines.".format(num_lines))
textfile = True
while textfile:
    print("\nInvalid Line will exit the program\nPress 0 to Exit")
    lines = int(input("Enter a line number: "))
    if lines == 0:
        textfile = False
    elif 1 > lines or lines > num_lines:
        textfile = False
    else:
        print(text_lines[lines - 1] )