shopping = []

choice = ""

while choice != "quit":
    choice = input("Enter add/remove/show/quit: ")

    if choice == "add":
        item = input("Enter item: ")
        shopping.append(item)

    elif choice == "remove":
        item = input("Enter item to remove: ")
        if item in shopping:
            shopping.remove(item)

    elif choice == "show":
        print(shopping)

print("Program ended")
