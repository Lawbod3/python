
def print_menu():
    menu = """
    To-Do List Manager
1. Add a task
2. View tasks
3. Mark task as complete
4. Delete a task
5. Exit
           """
    return print(menu)




def validate_add_task(addTask):
    
    try:

       if addTask.strip():
          return True
       else:
          return False

    except ValueError:
           return False

def validate_selection(selection):

    if selection < 1 or selection > 5:
       return False

    else:
       return True


def view_task(allTask):
    if not allTask:
       print("No task is added")

    else:
       for count, value in allTask.items():
           print(f"{count}. {value}")

def delete_task(allTask, number):
    if str(number) in allTask:
        allTask.pop(str(number))
    return allTask
    
def convert_to_string(selection):
    converter = str(selection)
    return converter   
    
    

    
    
    

def main():
    addTask: str
    allTask = {}
    selection = 0
    
    while True:
          print_menu()
          try:  
              selection = int(input("Enter a selection from(1-4): "))
              if selection < 1 or selection > 5:
                 print("Please let your input be from range of 1 to 5")

          except ValueError:
                 print("Please only input an Integer")
           
          if selection == 1:
              while True:
                    addTask = input("input your task: ")
                    if validate_add_task(addTask):
                       korkoro = convert_to_string(len(allTask) + 1) 
                       allTask[korkoro] = addTask
                       break  
                    else:
                      print("Your description cant be empty")

          elif selection == 2:
                print("\nTASK TO DO")
                view_task(allTask)

          elif selection == 3:
               while True:
                  if not allTask:
                     print("No task is added")
                     break

                  else:
                    try:
                       view_task(allTask)
                       selection = int(input("selecta task you have completed: "))
                       if convert_to_string(selection) not in allTask:
                             print("Selection is not in the option")
                    
                       else:
                           task_number = convert_to_string(selection)
                           allTask[task_number] = f" [X] {allTask[task_number]}"
                           print(f"{task_number}") 

                    except ValueError:
                           print("Please input only integers")

          elif selection == 4:
               while True:
                  if not allTask:
                     print("No task is added")
                     break

                  else:
                    view_task(allTask)
                    try:  
                       selection = int(input("select task to delete: "))
                       if convert_to_string(selection) not in allTask:
                          print("Selection is not in the option")
                     
                       else:
                         delete_task(allTask, convert_to_string(selection))
                         break
       
                    except ValueError:
                        print("Please only input an Integer")

          elif selection == 5:
               print("\nExiting the app....Goodbye.")
               break




               
              






if __name__ == "__main__":
    main()
  

    

    












    
