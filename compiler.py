from os import listdir, getcwd, system

def compiler_list():
    generalDir = []
    for file in listdir(getcwd()):
        if file.endswith(".cpp"):
            generalDir.append(file)
    return generalDir

def list_in_string(list):
    string = ""
    for element in list:
        string += f"{element} "
    return string

def console_execution(fileToCompile : list):
    print("Welcome to C++ Compiler")
    print(f"Files to compile: {list_in_string(fileToCompile)}\n")
    if system("cd output/") == 1:
        print("Creating output folder")
        system("mkdir output")
    
    if system(f"g++ {list_in_string(fileToCompile)}-o output\main.exe") == 1:
        print("\nC++ code is not good. Check it a little bit")
        return False
    else:
        print("Compile successfull\n")
        return True

def executing_program(query):
    if query == 0:
        print("That's right, GOOD BYE")
    elif query == 1:
        print("Executing main file")
        system(".\output\main.exe")