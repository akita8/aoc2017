def aoc3(inp):
    num = int(inp)
    i = 1
    j = 3
    while i <= num:
        if i == j**2:
            j+=2
        i+=1
    corner = j**2
    dist_from_corner = corner - num
    max_dist = j-1
    min_dist = int(max_dist/2)
    i = 1
    down = True
    distance = max_dist
    while i <= dist_from_corner:
        if down:
            distance -= 1
        else:
            distance += 1
        if distance == min_dist or distance == max_dist:
            down = not down
        i += 1
    return distance


def aoc3_2(inp):
    pass


if __name__ == "__main__":
    with open("aoc3_input.txt") as f:
        puzzle = str(f.read())
    print(aoc3(puzzle))
    print(aoc3_2(puzzle))