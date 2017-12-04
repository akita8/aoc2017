def aoc4(inp):
    valid = 0
    for line in inp.split('\n'):
        words = line.split(' ')
        if len(words) == len(set(words)):
            valid += 1
    return valid


def aoc4_2(inp):
    valid = 0
    for line in inp.split('\n'):
        words = [set(word) for word in line.split(' ')]
        for word in words:
            control = 0
            for other_word in words:
                if word == other_word:
                    control += 1
            if control > 1:
                break
        else:
            valid += 1
    return valid



if __name__ == "__main__":
    with open("aoc4_input.txt") as f:
        puzzle = str(f.read())
    print(aoc4(puzzle))
    print(aoc4_2(puzzle))
