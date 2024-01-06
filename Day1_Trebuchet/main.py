import regex

############## part1 ##############


def find_first_and_last_digit(s: str) -> int:
    digits = regex.findall(r"\d", s)

    as_str = digits[0] + digits[-1]

    return int(as_str)


with open("Day1_Trebuchet/data.txt", "r") as f:
    input_list = f.readlines()

list_part_one = []
for line in input_list:
    list_part_one.append(find_first_and_last_digit(line))

print("Answer for part 1 is: ", sum(list_part_one))

############## part2 ##############


def find_first_and_last_real_digit(s: str) -> int:
    digits = regex.findall(
        "\d|one|two|three|four|five|six|seven|eight|nine", s, overlapped=True
    )
    mapping = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    for index, digit in enumerate(digits):
        if digit in mapping.keys():
            digits[index] = mapping.get(digit)

    as_str = digits[0] + digits[-1]

    return int(as_str)


list_part_two = []
for line in input_list:
    list_part_two.append(find_first_and_last_real_digit(line))

print("Answer for part 2 is: ", sum(list_part_two))
