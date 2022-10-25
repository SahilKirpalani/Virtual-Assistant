
# Carry on and begin to take users questions
def carryon():
    carryon = input(
        "Would you like to ask me a question? Your wish is my command... Type 'yes' to continue")

    if carryon == 'Y' or 'y' or 'yes' or 'Yes':
        print("sweet dude...")
    elif carryon == 'N' or 'n' or 'No' or 'no':
        exit("Well I guess we'll see each other some other time... ")


carryon()
