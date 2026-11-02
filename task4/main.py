def parse_input(user_input: str):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args: str, contacts: dict):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def get_phone_num(name: str, contacts: dict):
    return contacts.get(name)


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(add_contact(args, contacts))
            print("Contact info changed")
        elif command == "phone":
            if args: 
                print(get_phone_num(args[0], contacts))
            else:
                print("Please provide username to get phone num")

        elif command == "all":
            print(contacts)
                    
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()