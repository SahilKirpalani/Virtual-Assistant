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


def question1():

    question_one = input(
        "Can we play a few games before I take your commands? (yes/no)")

    if question_one == 'Y' or 'y' or 'yes' or 'Yes':
        print("Ok let's continue... ")
    elif question_one == 'N' or 'n' or 'No' or 'no':
        exit("Bye!!!")

    print()


question1()

# Question 2 (Alphabet game)


def alphabetgame():

        alphabet = input("What is the 5th letter in the alphabet? ")

        if alphabet == 'e' or 'E':
            print("Correct! I see you're a smart one... ")
        else:
            print("Whoops. Could you please go back and learn these basics...")


alphabetgame()

# Question 3 (Favourite Movie)


def favoritemovie():
    movie = input("What is your favourite movie?")

    # Possible responses to user's favourite movie
    comments = [
        "Oh Nice!",
        "Thats a good one!",
        "I haven't seen " + movie,
        "REALLY!!! I can't beleive it. I hate " + movie,
        "Ive never heard of it.",
        "Omg! I die from laughter. It's so funny",
        "No way!, That's my favourite movie as well. Just jokes I hate it!"]

# Randomly display to comment on the user's favourite movie
    random_comment = random.choice(comments)
    print(random_comment)


favoritemovie()


def randomnumbergame():
    tries = 0
    number = r.randint(1, 20)
    guess = input('I am thinking of a number between 1 and 20. What is it? ')
    tries = tries + 1

    while True:
        if guess.isdigit():
            guess = int(guess)

            if guess > 20 or guess < 1:
                print('Guess between 1-20 ')

            elif guess > number:
                print('Too high')

            elif guess < number:
                print('Too low')

            else:
                print('You got it!')
                break

        else:
            print('Please guess a number.')
        guess = input('Try again: ')
        tries = tries + 1

    if tries == 1:
        print('You have got that after', tries, 'turn')
    else:
        print('That took you', tries, 'goes')


randomnumbergame()


# Carry on and begin to take users questions
def carryon():
    carryon = input(
        "Would you like to ask me a question? Your wish is my command... Type 'yes' to continue")

    if carryon == 'Y' or 'y' or 'yes' or 'Yes':
        print("sweet dude...")
    elif carryon == 'N' or 'n' or 'No' or 'no':
        exit("Well I guess we'll see each other some other time... ")


carryon()

# Begin asking user for commands to complete


def askuserforcommand():

    # loop to ask user question again
    use_again = True
    while use_again:

        command = input("How may I help you? ")

        # List of possible commands
        if command == "open google":
            webbrowser.open('http://www.google.com')

        elif command == "open youtube":
            webbrowser.open('http://www.youtube.com')

        elif command == "open mags website":
            webbrowser.open('https://www.mags.school.nz/')

        else:
            command = command
            print("Here are results on the internet...")
            webbrowser.open('https://www.google.com/search?q=' + command)

        # ask user if they would like to play again
        go_again = input("Would you like to play again. Yes, or No to exit...")
        if go_again == 'yes' or 'y' or 'Yes' or 'Y':
            use_again = True
        elif go_again == 'no' or 'n' or 'No' or 'N':
            print("Bye!!")


askuserforcommand()
