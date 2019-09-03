import os

os.system('clear')
checklist = list ()

#Create
def create (item):
    checklist.append(item)

#Read
def read(index):
    index = int(index)
    item = checklist[index]
    return item

#update
def update(index,item):
    index = int(index)
    checklist[index] = item

#destory
def destory (index):
    checklist.pop(index)

def list_all_items():
    index = 0
    for list_item in checklist:
        print("\033[1;33;40m{} \033[0;36m{}".format(index, list_item))
        index += 1
        

def mark_completed(index):
    update(index, "{}{}".format("√", checklist[int(index)]))

def mark_uncompleted(index):
    update(int(index), read(index)[1:])

def select(function_code):
    #Create item
    if function_code == "C":
        input_item = user_input("\033[0;32m create item:")
        create(input_item)
    #Read item
    elif function_code == "R":
        item_index = user_input("Read how many item?")
        read(item_index)
    #print all items
    elif function_code == "P":
        list_all_items()
    
    elif function_code == "U":
        item_index = input ("which item do you want to be updated: ")
        item_update = input("which item do you want instead")
        update(item_index, item_update)

    elif function_code == "RM":
        item_index = input ("which item do you want to remove from list")
        destory(item_index)
    
    elif function_code == "UC":
        mark_uncompleted()
        
    #elif function_code == ""
    elif function_code == "Q":
        #THis is where we want to stop out loop
        return False  
    
    else:
        print("Unknown Option")
    return True

def user_input(prompt):
    #the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input
#test
def test():
    create("purple sox")
    
    create("red cloak")
    
    print(read(0))
    
    update(0,"purple socks")
    destory(1)

    mark_completed(0)

    """print(read(0))
    list_all_items()

    mark_completed(0)

    mark_uncompleted(0)

    select("C")
    list_all_items()
    
    select("R")
    list_all_items()"""


    #user_value = user_input("Please Enter a value:")
    #print(user_value)


test()

running = True
while running: 
    selection = user_input(
    " Press C to create item to list\n R to Read item\n P to display all item\n U to update an item from list\n Press Q to Exit\n")
    running = select(selection)
