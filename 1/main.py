from utils import open_input_file


def elf_stock_from_input(filepath):
    input_data = open_input_file(filepath)
    elf_stock = input_data.split("\n\n")
    return [[int(v) for v in s.split("\n")] for s in elf_stock]


if __name__ == '__main__':
    stock = elf_stock_from_input("1/input.txt")

    # Part 1
    print(max([sum(v) for v in stock]))

    # Part 2
    print(sum(sorted([sum(v) for v in stock], reverse=True)[:3]))