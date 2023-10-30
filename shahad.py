

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

            n = int(input("Enter the number of elements (n): "))
            k = int(input("Enter the number of steps (k): "))
            
            array = input("Enter the array elements separated by spaces: ").split()
            k = k % n  # Adjust k to ensure it's within the array length
            
            rotated_array = array[-k:] + array[:-k]
            results= [int(row) for row in rotated_array]

            print("Output: ", results)

        elif choice == "3":
            # Display a simple help message
            print("\n--- Help --- \n")
            print("Option 1: Print a pattern with 'n' rows of decreasing asterisks.")
            print("Option 2: Rotate an array of 'n' elements to the right by 'k' steps.")
            print("Option 3: Display this help message.")
            print("Option 4: Exit the program.")

        elif choice == "4":
            # Exit the program
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice! Please select 1, 2, 3, or 4.")

        print("\n Please select an option:\n")
if __name__ == "__main__":
    main()