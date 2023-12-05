from compiler import compiler_list, console_execution, executing_program

def main():
    fileToCompile = compiler_list()
    if len(fileToCompile) == 0:
        print("Doesn't exist C++ files in this directory")
    else:
        exe = console_execution(fileToCompile)
        if exe:
            print("Do you wanna execute this program")
            query = int(input("(1 for yes, 0 for no): "))
            executing_program(query)

if __name__ == "__main__":
    main()