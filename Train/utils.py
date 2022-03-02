def read_input(input_file):
    with open(input_file) as f:
        line_1 = f.readline()
        line_2 = f.readline()

    return [line_1, line_2]


def sanitize_input(line):
    bogies = line.split(' ')
    if len(bogies[-1]) > 3:
        bogies[-1] = bogies[-1][:-1]
    return bogies
