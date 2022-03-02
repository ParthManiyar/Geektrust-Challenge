import sys
from utils import read_input, sanitize_input
from train import Train


def main():
    input_file = sys.argv[1]
    [line_1, line_2] = read_input(input_file)
    bogies_a = sanitize_input(line_1)
    bogies_b = sanitize_input(line_2)
    traina_obj = Train('A', bogies_a)
    trainb_obj = Train('B', bogies_b)
    bogies_arrived_hyderabad_a = traina_obj.bogies_arrived_hyderabad()
    bogies_arrived_hyderabad_b = trainb_obj.bogies_arrived_hyderabad()
    print(bogies_arrived_hyderabad_a)
    print(bogies_arrived_hyderabad_b)
    trainab = traina_obj.merge_trains(trainb_obj.bogies_arrived)
    print(trainab)


if __name__ == "__main__":
    main()
