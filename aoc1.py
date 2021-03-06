def aoc1(inp):
    i = 0
    ris = 0
    while i < len(inp):
        current_n = i
        next_n = i+1
        if next_n == len(inp):
            next_n = 0
        if inp[current_n] == inp[next_n]:
            ris = ris + int(inp[current_n])
        i = i+1
    return ris


def aoc1_2(inp):
    i = 0
    ris = 0
    offset = int(len(inp)/2)
    while i < len(inp):
        current_n = i
        next_n = i+offset
        if next_n >= len(inp):
            next_n = next_n -len(inp)
        if inp[current_n] == inp[next_n]:
            ris = ris + int(inp[current_n])
        i = i+1
    return ris


if __name__ == "__main__":
    with open("aoc1_input.txt") as f:
        puzzle = str(f.read())
    print(aoc1(puzzle))
    print(aoc1_2(puzzle))
