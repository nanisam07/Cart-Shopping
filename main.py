from cli_app import menu
from ui import run_ui


print("Choose Interface:")
print("1. CLI (Command Line)")
print("2. UI (Tkinter GUI)")

choice = input("Enter choice: ")

if choice == "1":
    menu()
elif choice == "2":
    run_ui()
else:
    print("Invalid choice!")
