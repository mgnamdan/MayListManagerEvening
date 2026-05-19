# ~~~~~~~~~~~~~~~~~~~~~~~~~
# IMPORTS AND HELPER FUNCTIONS
# ~~~~~~~~~~~~~~~~~~~~~~~~~
def loadList():
    try:
        with open("savedList.txt", "r") as file:
            loadedList = file.readlines()
            for idx in range(len(loadedList)):
                loadedList[idx] = loadedList[idx].strip("\n")
    except FileNotFoundError:
        loadedList = []
    finally:
        return loadedList



def saveList(listIn):
    with open("savedList.txt", "w") as file:
        for idx in range(len(listIn)):
            if idx == len(listIn) - 1:
                file.write(listIn[idx])
            else:
                file.write(f"{listIn[idx]}\n")



def displayList(listIn):
    print("")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("   LIST")
    print("")
    if len(listIn) == 0:
        print("- There are no items in the list! -")
    else:
        for idx in range(len(listIn)):
            print(f"{idx+1}. {listIn[idx]}")
    print("")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("")



def addItems(listIn):
    addMore = True
    editedList = listIn

    while addMore:
        displayList(editedList)
        print("Enter an item to add to the list (or 'done' to exit):")
        toAdd = input(" --> ")
        
        if toAdd.lower() in ["done", "quit", "exit"]:
            addMore = False
        else:
            editedList.append(toAdd)

    saveList(editedList)

    return editedList



def moveItems(listIn):
    moveMore = True
    editedList = listIn

    while moveMore:
        validMoveFrom = False
        while not validMoveFrom:
            displayList(editedList)
            print("Choose an item to move (or 'done' to exit):")
            toMoveFrom = input(" --> ")

            if toMoveFrom.lower() in ["done", "quit", "exit"]:
                moveMore = False
                validMoveFrom = True
                return editedList
            elif int(toMoveFrom) in range(len(editedList)):
                # Situation where an index number was given
                # Get thing at that position
                validMoveFrom = True
                pass
            elif toMoveFrom in editedList:
                # Situation where a list item was given
                validMoveFrom = True
                pass
            else:
                print("Invalid option - please choose again!")
        
        validMoveTo = False
        while not validMoveTo:
            print("Choose a position to move the item to:")
            toMoveTo = input(" --> ")

            if int(toMoveTo) in range(len(editedList)):
                # Move to that position
                validMoveTo = True
                pass
            elif toMoveTo in editedList:
                # Move to given item position
                # --> Find position of the given element
                validMoveTo = True
                pass
            else:
                print("Invalid option - please try again!")

        editedList.insert(toMoveTo, toMoveFrom)
        saveList(editedList)
        return editedList


def editItems(listIn):
    pass



def removeItems(listIn):
    pass



# ~~~~~~~~~~~~~~~~~~~~~~~~~
# MAIN FUNCTION DEFINITION
# ~~~~~~~~~~~~~~~~~~~~~~~~~
def main():
    appOn = True
    userList = loadList()

    while appOn:
        print("")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(" WELCOME TO THE LIST MANAGER! CHOOSE AN OPTION:")
        print("")
        print("1. View List")
        print("2. Add Item(s) to List")
        print("3. Move Item(s) on List")
        print("4. Edit Item(s) on List")
        print("5. Remove item(s) from List")
        print("6. Exit Application")
        print("")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("")
        userChoice = input(" --> ").lower()

        if userChoice in ["1", "1.", "view", "view list"]:
            displayList(userList)
        elif userChoice in ["2", "2.", "add", "add item", "add items"]:
            userList = addItems(userList)
        elif userChoice in ["3", "3.", "move", "move item", "move items"]:
            userList = moveItems(userList)
        elif userChoice in ["4", "4.", "edit", "edit item", "edit items"]:
            userList = editItems(userList)
        elif userChoice in ["5", "5.", "remove", "remove item", "remove items"]:
            userList = removeItems(userList)
        elif userChoice in ["6", "6.", "quit", "exit"]:
            appOn = False
        else:
            print("Invalid option - please choose again!")



# ~~~~~~~~~~~~~~~~~~~~~~~~~
# MAIN FUNCTION CALL
# ~~~~~~~~~~~~~~~~~~~~~~~~~
main()
