def create_sequence(raw_inp):
    sequence = []
    for raw_row in raw_inp.split("\n"):
        row = []
        for raw_el in raw_row.split('\t'):
            row.append(int(raw_el))
        sequence.append(row)
    return sequence


def find_min_max(num_list):
    min_n = num_list[0]
    max_n = num_list[0]
    i = 1
    while i < len(num_list):
        if num_list[i] < min_n:
            min_n = num_list[i]
        if num_list[i] > max_n:
            max_n = num_list[i]
        i = i + 1
    return min_n, max_n


def aoc2(inp):
    sequence = create_sequence(inp)
    ris_list = []
    for row in sequence:
        min_n, max_n = find_min_max(row)
        ris_list.append(max_n-min_n)
    ris = 0
    for num in ris_list:
        ris = ris + num
    return ris


if __name__ == "__main__":
    with open("aoc2_input.txt") as f:
        puzzle = str(f.read())
    print(aoc2(puzzle))
