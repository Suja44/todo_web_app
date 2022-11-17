
FIlEPATH="todos.txt"

def get_todos(filepath=FIlEPATH):
    with open(filepath,'r') as file:
        todos=file.readlines()
    return todos

def write_todos(todos,filepath=FIlEPATH):
    with open(filepath,'w') as file:
        file.writelines(todos)

# print(__name__)