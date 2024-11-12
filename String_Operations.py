import os

def checkSubstring():
    str1 = input("Enter String 1: ") 
    str2 = input("Enter String 2: ")
    if str2 in str1: 
        print(str2, "is a substring of", str1)
    else:
        print(str2, "is not a substring of", str1)
    input("Press Enter to continue...")

def countOccurrence():
    str_input = input("Enter a String: ")
    ch = input("Enter Character to check: ") 
    count = str_input.count(ch)
    print(ch, "found", count, "times in", str_input)
    input("Press Enter to continue...")

def replaceSubstring():
    str1 = input("Enter String 1: ") 
    str2 = input("Enter Substring: ")
    str3 = input("Enter Substring replacement: ") 
    if str2 in str1:
        str1 = str1.replace(str2, str3)
        print("Updated String:", str1)
    else:
        print(str2, "not found in", str1)
    input("Press Enter to continue...")

def toCapital():
    str_input = input("Enter a String: ") 
    print(str_input.upper())
    input("Press Enter to continue...")

def initMenu(): 
    choice = 0
    while choice != 5: 
        os.system('cls' if os.name == 'nt' else 'clear')
        print("1. Check if the String is a Substring of Another String")
        print("2. Count Occurrences of Character")
        print("3. Replace a Substring with Another Substring")
        print("4. Convert to Capital Letters")
        print("5. Exit")
        
        choice = int(input("Enter Your Choice: "))
        if choice in range(1, 6):
            if choice == 1:
                checkSubstring() 
            elif choice == 2:
                countOccurrence() 
            elif choice == 3:
                replaceSubstring() 
            elif choice == 4: 
                toCapital()
        else:
            print("Enter a Valid Choice") 
            input("Press Enter to continue...")

initMenu()
