"""
Write a python program that do the following:

- display the initial content of the array
- display a menu of options
- allow user to select item in the menu (check if valid)
- perform the selected option (you may prompt additional info to user when need)
- display the resulting values of the array

Note: 
- The program has an array variable containing 10 random numbers
- You may add other options and features
- Your program should be uploaded to github before 1:30pm
- Record a demo presenting your program
- Send the demo directly to my messenger

Example Output:

Array: [1, 4, 3, 4, 4, 5, 6 ,2 ,56, 200]
Menu:
 1 -> Add an element
 2 -> Insert an element
 3 -> Modify an element
 4 -> Delete an element
 5 -> Arrange in ascending order
 6 -> Arrange in descending order
What do you want to do? (1-6): 4
Enter the index you want to delete: 3
The element has been deleted
This is the new array: Array: [1, 4, 3, 4, 5, 6 ,2 ,56, 200]
"""

print("Give ten random numbers to be listed")
first = int(input("First Number: "))
second = int(input("Second Number: "))
third = int(input("Third Number: "))
fourth = int(input("Fourth Number: "))
fifth = int(input("Fifth Number: "))
sixth = int(input("Sixth Number: "))
seventh = int(input("Seventh Number: "))
eight = int(input("Eighth Number: "))
ninth = int(input("Ninth Number: "))
tenth = int(input("Tenth Number: "))
while True:
    list1 = [first, second, third, fourth, fifth, sixth, seventh, eight, ninth, tenth]
    print("------------------------------------------------------------------------------------------")
    print(list1)
    print("------------------------------------------------------------------------------------------")
    print("1 -> Add an element")
    print("2 -> Insert an element")
    print("3 -> Modify an element")
    print("4 -> Delete an element")
    print("5 -> Arrange in ascending order")
    print("6 -> Arrange in descending order")
    print("------------------------------------------------------------------------------------------")
    todo = input("What do you want to do? ")
    print("------------------------------------------------------------------------------------------")

    if todo == "1":
        wtnumber = input("What number do you want to add? ")
        print("------------------------------------------------------------------------------------------")
        list1.append(int(wtnumber))
        print()
        print("The number has been added to the list")
        print(list1)
        print("------------------------------------------------------------------------------------------")
        print("------------------------------------------------------------------------------------------")
        quit = input("Press 'q' to quit and any button to continue: ")
        print("------------------------------------------------------------------------------------------")
        if quit == "q":
            print("GOODBYE!")
            exit()
        else: 
            continue
                
    if todo == "2":
        wtnumber = input("What number do you want to insert? ")
        print("------------------------------------------------------------------------------------------")
        wtinsert = input("After what number do you want to insert it to? ")
        print("------------------------------------------------------------------------------------------")
        while True:
            if int(wtinsert) not in list1:
                print("There is no number '" + wtinsert + "' in the list")
                wtinsert = input("After what number do you want to insert it to? ")
            else:
                break
        gtindex = list1.index(int(wtinsert))
        gtindex += 1
        list1.insert(gtindex, int(wtnumber))
        print()
        print("The number has been inserted!")
        print(list1)
        print("------------------------------------------------------------------------------------------")
        print("------------------------------------------------------------------------------------------")
        quit = input("Press 'q' to quit and any button to continue: ")
        print("------------------------------------------------------------------------------------------")
        if quit == "q":
            print("GOODBYE!")
            exit()
        else: 
            continue

    if todo == "3":
        wtmodify = input("What number do you want to modify? ")
        print("------------------------------------------------------------------------------------------")
        while True:
            if int(wtmodify) not in list1:
                print("There is no number '" + wtmodify + "' in the list")
                wtmodify = input("What number do you want to modify? ")
                print("------------------------------------------------------------------------------------------")
            else:
                break
        gtindex = list1.index(int(wtmodify))
        wtchange = int(input("What number do you want to change it into? "))
        print("------------------------------------------------------------------------------------------")
        list1[gtindex] = wtchange
        print()
        print("The number has been modified!")
        print(list1)
        print("------------------------------------------------------------------------------------------")
        print("------------------------------------------------------------------------------------------")
        quit = input("Press 'q' to quit and any button to continue: ")
        print("------------------------------------------------------------------------------------------")
        if quit == "q":
            print("GOODBYE!")
            exit()
        else: 
            continue

    if todo == "4":
        wtdelete = input("What number do you want to delete? ")
        print("------------------------------------------------------------------------------------------")
        while True:
            if int(wtdelete) not in list1:
                print("There is no number '" + wtdelete + "' in the list")
                wtmodify = input("What number do you want to modify? ")
                print("------------------------------------------------------------------------------------------")
            else:
                break
        list1.remove(int(wtdelete))
        print()
        print("The number has been deleted!")
        print(list1)
        print("------------------------------------------------------------------------------------------")
        print("------------------------------------------------------------------------------------------")
        quit = input("Press 'q' to quit and any button to continue: ")
        print("------------------------------------------------------------------------------------------")
        if quit == "q":
            print("GOODBYE!")
            exit()
        else: 
            continue

    if todo == "5":
        list1.sort()
        print()
        print("The list has been arranged in ascending order!")
        print(list1)
        print("------------------------------------------------------------------------------------------")
        print("------------------------------------------------------------------------------------------")
        quit = input("Press 'q' to quit and any button to continue: ")
        print("------------------------------------------------------------------------------------------")
        if quit == "q":
            print("GOODBYE!")
            exit()
        else: 
            continue

    if todo == "6":
        list1.sort(reverse=True)
        print()
        print("The list has been arranged in descending order!")
        print(list1)
        print("------------------------------------------------------------------------------------------")   
        print("------------------------------------------------------------------------------------------")
        quit = input("Press 'q' to quit and any button to continue: ")
        print("------------------------------------------------------------------------------------------")
        if quit == "q":
            print("GOODBYE!")
            exit()
        else: 
            continue
    
    else:
        continue
