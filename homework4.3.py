def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."
def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter command: ")
        command, args = parse_input(user_input)

        if command in ('exit', 'close'):
            print("Good bye!")
            break
        elif command == 'hello':
            print("How can I help you?")
        elif command == 'add':
            print(add_contact(contacts, args))
        elif command == 'change':
            print(change_contact(contacts, args))
        elif command == 'phone':
            print(show_phone(contacts, args))
        elif command == 'all':
            print(show_all(contacts))
        else:
            print("Unknown command. Please try again.")

def parse_input(user_input):
    parts = user_input.strip().split(maxsplit=1)
    command = parts[0].lower()
    args = parts[1] if len(parts) > 1 else ""
    return command, args

def add_contact(contacts, args):
    parts = args.split()
    if len(parts) != 2:
        return "Invalid input. Use: add [username] [phone]"
    name, phone = parts
    contacts[name] = phone
    return "Contact added."

def change_contact(contacts, args):
    parts = args.split()
    if len(parts) != 2:
        return "Invalid input. Use: change [username] [phone]"
    name, phone = parts
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."

def show_phone(contacts, args):
    name = args.strip()
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."

def show_all(contacts):
    if not contacts:
        return "No contacts found."
    result = ""
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result.strip()

if __name__ == "__main__":
    main()
