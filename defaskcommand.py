import webbrowser

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
            exit("Bye!!")


askuserforcommand()
