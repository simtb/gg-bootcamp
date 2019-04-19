import random


def password_generator(length_of_password, lower_case=True, upper_case=False, digits=False, special_characters=False):
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    special = "!@£$%^&*()-_+=:;?,."
    available_characters = ""

    if lower_case:
        available_characters += lowercase
    if upper_case:
        available_characters += uppercase
    if digits:
        available_characters += numbers
    if special_characters:
        available_characters += special

    generated_password = ""
    length_of_avaiable_characters = len(available_characters)

    for i in range(length_of_password):
        random_index = random.randint(0, length_of_avaiable_characters - 1)
        generated_password += available_characters[random_index]

    return generated_password


if __name__ == "__main__":
    print("Random Password Generator")
    print()
    print("Enter Password Length:")
    password_length = int(input())
    print("Password to contain upper case characters? y/n:")
    upper_case = input()
    print("Password to contain digits? y/n:")
    digits = input()
    print("Password to contain special characters? y/n:")
    special_characters = input()

    convert_to_boolean = {"y": True, "n": False}
    print(convert_to_boolean.get(special_characters))

    print(password_generator(password_length, lower_case=True, upper_case=convert_to_boolean.get(upper_case), digits=convert_to_boolean.get(digits), special_characters=convert_to_boolean.get(special_characters)))