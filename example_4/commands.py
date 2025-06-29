from storage import add_contact, change_contact, show_phone, show_all


def execute_command(command, args):
    """
    Виконує команду на основі введеного користувачем.
    """
    try:
        if command == "hello":
            return "How can I help you?"
        elif command == "add":
            if len(args) != 2:
                return "Invalid command. Use: add [username] [phone]"
            return add_contact(args[0], args[1])
        elif command == "change":
            if len(args) != 2:
                return "Invalid command. Use: change [username] [new_phone]"
            return change_contact(args[0], args[1])
        elif command == "phone":
            if len(args) != 1:
                return "Invalid command. Use: phone [username]"
            return show_phone(args[0])
        elif command == "all":
            return show_all()
        else:
            return "Invalid command. Please try again."
    except Exception as e:
        return f"An error occurred: {e}"
