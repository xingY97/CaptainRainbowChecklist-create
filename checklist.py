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
    checklist[index] = item

#destory
def destory (index):
    checklist.pop(index)

def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        #print(str(index) + list_item)
        index += 1
def mark_completed(index):
    update(index, "{}{}".format("√", checklist[int(index)]))

def select(function_code):
    #Create item
    if function_code == "C":
        input_item = user_input("Input item:")
        create(input_item)
    #Read item
    elif function_code == "R":
        item_index = user_input("input Number?")

        read(item_index)
    #print all items
    elif function_code == "P":
        list_all_items()
    elif function_code == "Q":
        #THis is where we want to stop out loop
        return False  
    #Catch all
    else:
        print("Unknown Option")

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
    print(read(1))
    
    update(0,"purple socks")
    destory(1)

    print(read(0))

    mark_completed(0)
   
    list_all_items()

    #Your testing code here
    #...
    #call your new function with the appropriate value
    select("C")
    #View the results
    list_all_items()
    #Call function with new value
    select("R")
    #View results
    list_all_items()
    #Continue until all code is run

    user_value = user_input("Please Enter a value:")
    print(user_value)


test()
running = True
while running: 
    selection = user_input(
    "Press C to add to list, R to Read from list and P to display list")
    running = select(selection)
