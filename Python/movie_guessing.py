points = [0, 0]
turn = 0
while True:
    print(
        "player ",
        turn + 1,
        " will give movie name and player",
        (turn + 1) % 2 + 1,
        " will guess movie",
    )
    name = input("give movie name")
    movie = list(name)
    movie_name = []
    g_movie = []
    for i in range(len(movie)):
        for j in range(len(movie[i])):
            if movie[i][j] == " ":
                movie_name.append(" ")
                g_movie.append(" ")
            else:
                movie_name.append(movie[i][j])
                g_movie.append("*")
    chance = 7
    print("Guess movie name\n ", "".join(g_movie))
    while g_movie != movie_name:
        if chance == 0:
            print("Your chances are over.Game over!!")
            break
        letter = input("enter the guessing letter")
        if letter in movie_name:
            for i in range(len(movie_name)):
                if movie_name[i] == letter:
                    g_movie[i] = letter
            print("".join(g_movie))
        else:
            chance = chance - 1
            print("Wrong guess!! Only ", chance, " chances are left!!")
    else:
        points[turn] = points[turn] + 1
        print(
            "Your points is ",
            points[turn],
            " and opponent point is ",
            points[(turn + 1) % 2],
        )
    turn = (turn + 1) % 2
