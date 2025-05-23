# Day 24 - Extended Notes App with seek(), tell(), and error handling (Notes App Version-2).

# This is the constant value where our notes will be stored.
NOTES_FILE = "notes.txt"

# This function displays the menu to the user to choose the operations to perform on file.
def show_menu():
    print("\n📘 Notes App v2 - File Cursor Mode")
    print("1. Add Note")
    print("2. View All Notes")
    print("3. Update Note")
    print("4. Delete Note")
    print("5. Show Cursor Position")
    print("6. Read from Byte Position")
    print("7. Exit")

# This function is used to add a note into our notes by appending and also handles the exceptions
def add_note():
    try:
        note = input("📝 Enter your note: ")
        with open(NOTES_FILE, "a") as f:
            f.write(note + "\n")
        print("✅ Note added.")
    except Exception as e:
        print(f"❌ Error adding note: {e}")

# This function is used to view the existing notes that are there in our notes file by reading and also handles the exceptions
def view_notes():
    try:
        with open(NOTES_FILE, "r") as f:
            notes = f.readlines()
            if not notes:
                print("📭 No notes yet.")
            else:
                print("\n📖 Your Notes:")
                for i, note in enumerate(notes, 1):
                    print(f"{i}. {note.strip()}")
    except FileNotFoundError:
        print("🚫 Notes file not found.")

# This function is used to update the notes based on a specific index number. Asks the user for index number of the note to update and 
# asks the new content to overwrite that specific note and also handles exception
def update_note():
    try:
        with open(NOTES_FILE, "r") as f:
            notes = f.readlines()
        view_notes()
        idx = int(input("✏️ Enter note number to update: ")) - 1
        if 0 <= idx < len(notes):
            updated = input("🔁 Enter updated note: ")
            notes[idx] = updated + "\n"
            with open(NOTES_FILE, "w") as f:
                f.writelines(notes)
            print("✅ Note updated.")
        else:
            print("⚠️ Invalid note number.")
    except Exception as e:
        print(f"❌ Error: {e}")

# This function is used to delete the note based on the specified index number of note. asks the user to note to delete and then deletes it
# by returning the deleted note and also handles exceptions
def delete_note():
    try:
        with open(NOTES_FILE, "r") as f:
            notes = f.readlines()
        view_notes()
        idx = int(input("❌ Enter note number to delete: ")) - 1
        if 0 <= idx < len(notes):
            deleted = notes.pop(idx)
            with open(NOTES_FILE, "w") as f:
                f.writelines(notes)
            print(f"✅ Deleted: {deleted.strip()}")
        else:
            print("⚠️ Invalid note number.")
    except Exception as e:
        print(f"❌ Error: {e}")

# Opens the file in read mode and displays the current cursor position in bytes using tell(). If the file doesn't exist, 
# it catches the FileNotFoundError.
def show_cursor_position():
    try:
        with open(NOTES_FILE, "r") as f:
            print(f"📍 Current cursor position: {f.tell()} bytes")
    except FileNotFoundError:
        print("🚫 File not found.")


# Asks the user for a byte position and uses seek() to move the cursor to that position in the file, then reads and displays the 
# content from that point onwards. It handles various exceptions such as invalid input or file not found.
def read_from_position():
    try:
        pos = int(input("🔎 Enter byte position to seek: "))
        with open(NOTES_FILE, "r") as f:
            f.seek(pos)
            data = f.read()
            if data:
                print("\n📄 Notes from position:")
                print(data)
            else:
                print("📭 No content after this position.")
    except ValueError:
        print("⚠️ Please enter a valid integer position.")
    except FileNotFoundError:
        print("🚫 Notes file not found.")
    except Exception as e:
        print(f"❌ Error reading from position: {e}")


# main
def main():
    # This loop runs until the user chooses to quit by breaking the loop
    while True:
        # This displays the menu to choose the option for user
        show_menu()
        # Takes the input of choice
        choice = input("👉 Enter choice: ")
        # If the user choose option 1 then it calls add_note()
        if choice == '1':
            add_note()
        # If the user choose option 2 then it calls view_notes()
        elif choice == '2':
            view_notes()
        # If the user choose option 3 then it calls update_note()
        elif choice == '3':
            update_note()
        # If the user choose option 4 then it calls delete_note()
        elif choice == '4':
            delete_note()
        # If the user choose option 5 then it calls show_cursor_position()
        elif choice == '5':
            show_cursor_position()
        # If the user choose option 6 then it calls read_from_position()
        elif choice == '6':
            read_from_position()
        # If the user choose option 7 the loop breaks and exits the app by a msg to user
        elif choice == '7':
            print("👋 Exiting Notes App v2...")
            break
        # If the user choose an invalid option then it displays this msg
        else:
            print("⚠️ Invalid choice. Try again.")



# calling main() to starting execution of program
if __name__ == "__main__":
    main()
