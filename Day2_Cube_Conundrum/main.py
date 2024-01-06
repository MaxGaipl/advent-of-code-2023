import re


def run_task1():
    solution_sum = 0
    COLORS = ["red", "green", "blue"]
    BAG_LOADED_WITH = {"red": 12, "green": 13, "blue": 14}

    with open("Day2_Cube_Conundrum/data.txt", "r") as f:
        for game in f.readlines():
            game_possible = True
            game_contents = re.search(
                r"Game (?P<game_id>\d+): (?P<draws>.*)$",
                game,
            )
            draws = re.split(
                ";",
                game_contents["draws"],
            )

            for draw in draws:
                for color in COLORS:
                    drawn_cubes = re.search(rf"(?P<{color}>\d+) {color}", draw)
                    if drawn_cubes:
                        drawn_cubes = int(drawn_cubes[color])

                        if drawn_cubes > BAG_LOADED_WITH[color]:
                            game_possible = False

            if game_possible:
                game_id = int(game_contents["game_id"])
                solution_sum += game_id

        return solution_sum


def run_task2():
    solution_sum = 0
    COLORS = ["red", "green", "blue"]

    with open("Day2_Cube_Conundrum/data.txt", "r") as f:
        for game in f.readlines():
            game_possible = True
            game_contents = re.search(
                r"Game (?P<game_id>\d+): (?P<draws>.*)$",
                game,
            )
            draws = re.split(
                ";",
                game_contents["draws"],
            )

            max_cubes_of_color = {"red": 0, "green": 0, "blue": 0}

            for draw in draws:
                for color in COLORS:
                    drawn_cubes = re.search(rf"(?P<{color}>\d+) {color}", draw)
                    if drawn_cubes:
                        drawn_cubes = int(drawn_cubes[color])

                        if max_cubes_of_color[color] < drawn_cubes:
                            max_cubes_of_color[color] = drawn_cubes

            power = (
                max_cubes_of_color["red"]
                * max_cubes_of_color["green"]
                * max_cubes_of_color["blue"]
            )
            solution_sum += power

    return solution_sum


if __name__ == "__main__":
    print(run_task2())
