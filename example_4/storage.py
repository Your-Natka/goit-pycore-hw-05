from error_handlers import input_error

contacts = {}

@input_error
def add_contact(name, phone):
    """
    Додає новий контакт.
    """
    contacts[name] = phone
    return f"Contact '{name}' added with phone '{phone}'."

@input_error
def change_contact(name, new_phone):
    """
    Змінює існуючий контакт.
    """
    if name in contacts:
        contacts[name] = new_phone
        return f"Contact '{name}' updated with new phone '{new_phone}'."
    return f"Contact '{name}' not found."

@input_error
def show_phone(name):
    """
    Виводить номер телефону для вказаного імені.
    """
    if name in contacts:
        return f"{name}: {contacts[name]}"
    return f"Contact '{name}' not found."

@input_error
def show_all():
    """
    Виводить усі контакти та номери телефонів.
    """
    if not contacts:
        return "No contacts found."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
