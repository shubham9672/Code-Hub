import random
def main():
    special_letters = "?!_.,;:*-~"
    name = input("Name: ")
    surname = input("Surname: ")
    goal = input("What's this password for: ")
    username = input("What's your username: ")
    sequence = []
    for i in range(4):
        name_rnd = random.randint(0,len(name)-1)
        surname_rnd = random.randint(0,len(surname)-1)
        char_rnd = random.randint(0,len(special_letters)-1)
        sequence.append(name[name_rnd] + surname[surname_rnd] + special_letters[char_rnd])
    with open("log.txt", "a") as f:
        f.write("This password is for {0}. Username: {2} | Password: {1}\n".format(goal, "".join(sequence), username))

if __name__ == "__main__":
    main()