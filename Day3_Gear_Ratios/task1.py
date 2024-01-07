import re


def get_number_positions_in_str(input: str) -> list[str]:
    number_pattern = r"(?:\d+)"
    number_positions_in_line = []
    numbers = re.finditer(number_pattern, input.strip())
    for number in numbers:
        number_position = [number.start(), number.end()]
        number_positions_in_line.append(number_position)

    return number_positions_in_line


def is_number_next_to_symbol(
    engine_schematic: list[str], line: str, number_position: list[int]
) -> bool:
    check_strings = generate_check_strings(engine_schematic, line, number_position)

    if any(is_regex_in_str(check_string, r"[^\d.]") for check_string in check_strings):
        return True


def is_regex_in_str(check_str: str, regex_pattern: str) -> bool:
    regex_in_str = re.match(
        regex_pattern,
        check_str,
    )
    if regex_in_str:
        return True


def generate_check_strings(engine_schematic, line, number_position):
    check_strings = []
    start_search_at = number_position[0] - 1 if number_position[0] - 1 > 0 else 0
    end_search_at = (
        number_position[1] + 1
        if number_position[1] + 1 < len(engine_schematic[line])
        else len(engine_schematic[line]) - 1
    )
    check_strings.append(engine_schematic[line][start_search_at:end_search_at])
    if line > 0:
        check_strings.append(engine_schematic[line - 1][start_search_at:end_search_at])
    if line < len(engine_schematic) - 1:
        check_strings.append(engine_schematic[line + 1][start_search_at:end_search_at])
    return check_strings


def run_task_1():
    with open("Day3_Gear_Ratios/data.txt", "r") as file:
        engine_schematic = file.readlines()
        valid_numbers = []
        number_schema = []
        for str in engine_schematic:
            number_schema.append(get_number_positions_in_str(str))

        for line, line_str in enumerate(engine_schematic):
            for position in number_schema[line]:
                number_valid = is_number_next_to_symbol(
                    engine_schematic=engine_schematic,
                    line=line,
                    number_position=position,
                )

                if number_valid:
                    valid_numbers.append(int(line_str[position[0] : position[1]]))

    print(f"The sum of all part numbers is {sum(valid_numbers)}")


if __name__ == "__main__":
    run_task_1()
