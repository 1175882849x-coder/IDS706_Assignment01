def welcome_message(name):
    """return welcome text with provided name parameter"""
    return f"{name}, welcome to the Data Engineering course."


if __name__ == "__main__":
    name = input("Enter your name: ")
    print(welcome_message(name))
