from Linkedlist.node import Node
from Linkedlist.linked_list import linkedList

def main():
    my_list = linkedList()

    while True:
        print("\n=== Linked List Menu ===")
        print("1. Insert Node")
        print("2. Delete Node")
        print("3. Print List")
        print("4. Count Nodes")
        print("5. Find Node")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            value = int(input("Enter value to insert: "))
            my_list.insert_node(value)
            print(f"{value} inserted into the list.")

        elif choice == '2':
            value = int(input("Enter value to delete: "))
            if my_list.delete_node(value):
                print(f"{value} deleted from the list.")
            else:
                print(f"{value} not found in the list.")

        elif choice == '3':
            print("Linked List:")
            my_list.print_items()

        elif choice == '4':
            count = my_list.count_nodes()
            print(f"Total nodes in the list: {count}")

        elif choice == '5':
            value = int(input("Enter value to find: "))
            if my_list.find_node(value):
                print(f"{value} found in the list.")
            else:
                print(f"{value} not found in the list.")

        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
