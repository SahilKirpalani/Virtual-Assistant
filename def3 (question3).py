import random
import random as r

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
