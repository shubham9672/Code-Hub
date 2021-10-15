def floyd_triangle(max_line):
    number = 1
    for i in range(1, max_line + 1):
        for i in range(i):
            print(f"{number} ", end="")
            number += 1
        print()


max_line = int(input("Max line for floyd pyramid: "))

floyd_triangle(max_line)
