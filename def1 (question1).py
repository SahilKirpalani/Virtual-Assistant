def question1():

    question_one = input(
        "Can we play a few games before I take your commands? (yes/no)")

    if question_one == 'Y' or 'y' or 'yes' or 'Yes':
        print("Ok let's continue... ")
    elif question_one == 'N' or 'n' or 'No' or 'no':
        exit("Bye!!!")

    print()


question1()