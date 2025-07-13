from stack import Stack

def main():
    my_stack = Stack()


    while True:
        print("\n=== Stack Operations Menu ===")
        print("1. Push ")
        print("2. Pop")
        print("3. Peek")
        print("4. Is Empty")
        print("5. Length of Stack")
        print("6. Print stack elements")
        print("7. Exit")

        choice = input("Enter your choice (1-7)")

        match choice:
            case '1':
               value = int(input("Enter value to insert: "))
               my_stack.push(value)
               print(f"{value} pushed to stack")
            case '2':
                value=my_stack.pop()
                print(f"{value} poped from stack ")
            case '3':
                print(f"{ my_stack.peek() } is the peek value")
            case '4':
                if my_stack.isEmpty():
                    print("The Stack is Empty")
                else:
                    print("Stack is not Empty")
            case '5':
                print(f" Length is {my_stack.length()}")
            case '6':
                my_stack.print_elements()
            case '7':
                print("Exiting...")
                break
            case _:
                print("Enter valid number between 1 to 7")


if __name__ == "__main__":
    main()

