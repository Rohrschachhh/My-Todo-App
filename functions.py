
FilePath = "todos.txt"

def get_tasks(filepath = FilePath):            
    """ Read a text file and return the list of to-do items.(objects) """
    
    with open(filepath, 'r') as file:                          #improves file handling
        task_list = file.readlines()                         
    return task_list

def write_tasks(filename, filepath = FilePath):       
    """ Write the to-do items list in a text file. """
    
    with open(filepath, 'w') as file:
        file.writelines(filename)