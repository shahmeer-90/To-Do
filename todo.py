# todo.py

todos = []

def add_todo(title, date):
    todos.append({"title": title, "date": date})

def view_todos():
    if not todos:
        print("\nNo todos available.")
    else:
        print("\nYour To-Do List:")
        for i, todo in enumerate(todos, start=1):
            print(f"{i}. {todo['title']} - {todo['date']}")

def delete_todo(index):
    if 0 <= index < len(todos):
        removed = todos.pop(index)
        print(f"Removed: {removed['title']}")
    else:
        print("Invalid index!")

def delete_all():
    todos.clear()
    print("All todos deleted.")

def main():
    while True:
        print("\n--- To-Do Application ---")
        print("1. Add To-Do")
        print("2. View To-Dos")
        print("3. Delete a To-Do")
        print("4. Delete All To-Dos")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter To-Do title: ")
            date = input("Enter date (YYYY-MM-DD): ")
            add_todo(title, date)

        elif choice == "2":
            view_todos()

        elif choice == "3":
            view_todos()
            try:
                index = int(input("Enter number to delete: ")) - 1
                delete_todo(index)
            except ValueError:
                print("Invalid input!")

        elif choice == "4":
            delete_all()

        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
