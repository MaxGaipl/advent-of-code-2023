import math
import re

from utils.utils import timeit


@timeit
def run():
    with open("data/Day4.txt", "r") as file:
        cards = file.readlines()

    points = 0
    for card in cards:
        numbers = card.strip().split(sep=":")[1].split(sep="|")
        winning_numbers = [
            int(number) for number in re.findall(pattern="(?:\d+)", string=numbers[0])
        ]
        card_numbers = [
            int(number) for number in re.findall(pattern="(?:\d+)", string=numbers[1])
        ]

        number_of_winning_numbers = 0
        for number in card_numbers:
            if number in winning_numbers:
                number_of_winning_numbers += 1

        if number_of_winning_numbers >= 1:
            points += math.exp2(number_of_winning_numbers - 1)

    print(f"You have {points} points")


if __name__ == "__main__":
    run()
