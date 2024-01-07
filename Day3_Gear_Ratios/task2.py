import re


def get_possible_gear_positions(input: list[str]) -> bool:
    gear_pattern = r"(?:\*)"
    possible_gear_positions = []
    for line, str in enumerate(input):
        gears = re.finditer(gear_pattern, str.strip())
        for gear in gears:
            gear_position = [line, gear.start(), gear.end()]
            possible_gear_positions.append(gear_position)

    return possible_gear_positions


def get_gear_relevant_numbers(input: list[str], gear_position: list[int]) -> list[str]:
    possible_gear_range_horizontal = range(gear_position[1] - 1, gear_position[2] + 1)
    possible_lines = range(gear_position[0] - 1, gear_position[0] + 2)
    relevant_numbers: list[int] = []
    for line in possible_lines:
        number_pattern = r"(?:\d+)"
        numbers = re.finditer(number_pattern, input[line].strip())

        for number in numbers:
            number_area = range(number.start(), number.end())

            if any(
                position in number_area for position in possible_gear_range_horizontal
            ):
                relevant_numbers.append(
                    int(input[line].strip()[number.start() : number.end()])
                )

    return relevant_numbers


def run_task_2():
    with open("Day3_Gear_Ratios/data.txt", "r") as file:
        engine_schematic = file.readlines()

        gear_ratios = []

        possible_gear_positions = get_possible_gear_positions(engine_schematic)
        for gear_position in possible_gear_positions:
            relevant_numbers = get_gear_relevant_numbers(
                engine_schematic, gear_position
            )
            if len(relevant_numbers) == 2:
                gear_ratio = relevant_numbers[0] * relevant_numbers[1]
                gear_ratios.append(gear_ratio)

    print(f"The sum of all part numbers is {sum(gear_ratios)}")


if __name__ == "__main__":
    run_task_2()
