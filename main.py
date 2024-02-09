import random
from DATA import data


def follower(index):
    follower = (data[index])["follower_count"]
    return follower


def person(index):
    person = (data[index])["name"]
    return person


def decr(index):
    desc = (data[index])["description"]
    return desc


def reg(index):
    region = (data[index])["country"]
    return region


print("Welcome to the INSTAGRAM FOLLOWERS GUESSING GAME")
over = True
while over:
    namee = input("Please tell us your name: ")
    if namee.isalpha():
        over = False
    else:
        print("Name can't contain digits. Try again....\n")

up = 0
name = ""
for i in namee:
    up += 1
    if up == 1:
        name += i.upper()
    else:
        name += i.lower()

end_game = False
score = 0
a = random.randint(0, len(data) - 1)
okay = 0
while not end_game:
    if okay > 0:
        a = b
    rechoose = True
    while rechoose:
        b = random.randint(0, len(data) - 1)
        if a != b:
            rechoose = False
    comparea = f"\nCompare A: {person(a)}, a {decr(a)}, from {reg(a)}."
    compareb = f"Against B: {person(b)}, a {decr(b)}, from {reg(b)}."
    print(comparea)
    print("""
        VVVVSSSSSSS
    """)
    print(compareb)

    end = False
    while not end:
        who = input("Who has more Instagram followers: ").upper()
        if who == "A" or who == "B":
            end = True
        else:
            print("Input can only be 'A' or 'B'. Try again....\n")
    A = follower(a)
    B = follower(b)

    if who == "A":
        who = A
        notwho = B
    else:
        who = B
        notwho = A

    # print(who)
    # print(notwho)

    if who > notwho:
        result = "you win!!!"
        okay += 1
    elif who < notwho:
        result = "you lose!"
    else:
        result = "it's a draw!!"

    print("Dear " + name + ", " + result)

    if result == "you lose!":
        print(f"\nFinal score = {score}")
        score = 0
        more = True
        while more:
            again = input("\nDo you wish to play again? (y/n): ").lower()
            if again == "y" or again == "n":
                more = False
            else:
                print("Input can only be 'y' or 'n'....")
        print("\n")
        if again == "n":
            print("Goodbye " + name + ", we're looking forward to seeing you again, very soon.\nTAKE CARE!")
            end_game = True
            break
        else:
            okay = 0
            a = random.randint(0, len(data) - 1)
    elif result == "you win!!!":
        score += 1.5
        print(f"Current score: {score}")
    else:
        score += 0
        print(f"Current score: {score}")








