# Author: Aaron Rumbold
# Course: HND Digital Technologies for England (Cyber Security)
# 		  Unit 4 - Programming (2025)
# License: MIT

def save_report_to_file():
    pass

def save_csv_to_file():
    pass

def save_list_to_file(todo_list, filename="todo_list.txt"):
    """ Save the to-do list to a file. """

    try:
        with open(filename, 'w') as file:
            for item in todo_list:
                file.write(f"{item}\n")
        print(f"To-do list saved to {filename}.")
    except Exception as e:
        print(f"An error occurred while saving the list: {e}")


def load_list_from_file(filename="todo_list.txt"):
    """ Load the to-do list from a file. """

    try:
        with open(filename, 'r') as file:
            todo_list = [line.strip() for line in file.readlines()]
        print(f"To-do list loaded from {filename}.")
        return todo_list
    except FileNotFoundError:
        print(
            f"No existing to-do list found at {filename}. "
            "Starting a new list."
        )
        return []




def add_item(todo_list, item):
    """ Add a new item to the to-do list. """

    if (item in todo_list):
        print(f"The item '{item}' is already in the list.")
    else:
        todo_list.append(item)
        print(f"The item '{item}' has been added to the list.")
    pass


def remove_item(todo_list, item):
    """ Remove an item from the to-do list. """

    if item in todo_list:
        todo_list.remove(item)
        print(f"The item '{item}' has been removed from the list.")
    else:
        print(f"The item '{item}' did not exist in your list.")


def display_list(todo_list):
    """ Display all items in the to-do list. """

    if not todo_list:
        print("The to-do list is empty.")
    else:
        print("To-Do List:")
        for index, item in enumerate(todo_list, start=1):
            print(f"{index}. {item}")




def main():
    """ Main function to run the to-do list program. """
    todo_list = []

    while True:
        item = input("\nEnter a to-do item\n(or 'help' for more options"
                     " or 'exit' to quit): ")
        if item.lower() == 'exit':
            break
        elif item.lower() == 'help':
            print("\nOptions:")
            print(" - Type the item name to add it to the list.")
            print(" - Type 'remove <item>' to remove an item from the list.\n"
                  "    Example: 'remove Buy groceries' to remove that item.")
            print(" - Type 'show'"
                  " or 'display' to show all items in the list.")
            print(" - Type 'save' to save the list to a file.")
            print(" - Type 'load' to load the list from a file.")
            print(" - Type 'exit' to quit the program.")
            print(" - Type 'help' to display this help message again.")
        elif item.lower() == 'save':
            save_list_to_file(todo_list)
        elif item.lower() == 'load':
            todo_list = load_list_from_file()
        elif item.startswith('remove '):
            # Extract the item to remove
            item_to_remove = item[len('remove '):]
            remove_item(todo_list, item_to_remove)
        elif item == 'show' or item == 'display':
            display_list(todo_list)
        elif item.startswith('add '):
            item_to_add = item[len('add '):]
            add_item(todo_list, item_to_add)
        else:
            add_item(todo_list, item)


if __name__ == "__main__":
    main()




__all__ = [save_report_to_file,save_csv_to_file]