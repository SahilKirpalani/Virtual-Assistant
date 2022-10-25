import webbrowser
import random
import random as r

# Ask user for name
user_name = input("What is your name? ").capitalize()

print()

# Welcome statement


def greeting():
    print("Hi " + user_name, "My name is Vecna!")

    print()


greeting()

# introduce user to how virtual assistant works
user_introduction = [
    "|    Welcome. I am your virtual chatbot    |",
    "|           - Let's have a chat..          |",
    "|               - You answer...            |",
    "|       - I dont use your microphone...    |",
    "|        - So your privacy is safe...      |", ]
print()

# chat with user before completing commands
