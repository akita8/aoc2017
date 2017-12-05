def aoc5(inp):
    steps = 0
    pos = 0
    instructions = [int(num) for num in inp.split('\n')]
    while pos < len(instructions):
        next_step = instructions[pos]
        instructions[pos] = next_step + 1
        pos += next_step
        steps +=1
    return steps


def aoc5_2(inp):
    steps = 0
    pos = 0
    instructions = [int(num) for num in inp.split('\n')]
    while pos < len(instructions):
        next_step = instructions[pos]
        if next_step >= 3:
            instructions[pos] = next_step - 1
        else:
            instructions[pos] = next_step + 1
        pos += next_step
        steps +=1


    return steps


if __name__ == "__main__":
    with open("aoc5_input.txt") as f:
        puzzle = str(f.read())
    print(aoc5(puzzle))
    print(aoc5_2(puzzle))