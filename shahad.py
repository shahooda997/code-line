

def main():
    print("Welcome to the Menu-Based Program!\n")

    print("Please select an option:\n")
    
    # Display the menu
    print("1- Print Pattern")
    print("2- Rotate Array")
    print("3- Help")
    print("4- Exit")
    print("\n")
    while True:
        choice = input("Option: ")

        if choice == "1":
            # Get number from user and print pattern
            num = int(input("Enter the number of rows for the pattern:")) 
            print("Output:\n")
            for i in range(num, 0, -1):
                print('* ' * i)
            
        
            

        elif choice == "2":
            # Get array details from user and rotate it
            n = int(input("Enter the number of elements n: "))
            k = int(input("Enter the number of steps k: "))
            
            array = input("Enter {} numbers separated by spaces: ".format(n)).split()
            k = k % n  # Adjust k to ensure it's within the array length
            
            rotated_array = array[-k:] + array[:-k]
            print("Rotated Array:", rotated_array)

        elif choice == "3":
            # Display a simple help message
            print("\n Select 1 to print a pattern, 2 to rotate numbers, 3 for help, or 4 to exit.")

        elif choice == "4":
            # Exit the program
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Please select 1, 2, 3, or 4.")

        print("\n Please select an option:\n")
if __name__ == "__main__":
    main()