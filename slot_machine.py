import random

MAX_LINE = 3
MAX_BET = 500
MIN_BET = 10

Rows = 3
Columns = 3

symbols_count = {
    "👑": 2,
    "🍌": 4,
    "🥝": 6,
    "🍒": 8
}

symbols_value = {
    "👑": 10,
    "🍌": 5,
    "🥝": 3,
    "🍒": 2
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def get_slot_machine_spin(rows, columns, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    cols = []
    for _ in range(columns):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        cols.append(column)
    return cols


def print_slot_machine(columns):
    for row in range(len(columns)):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()


def deposit():
    while True:
        amount = input("How much do you want deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Please add number greater than 0")
        else:
            print("Please add number")
    return amount


def get_number_of_lines():
    while True:
        lines = input("How many lines do you want to have(1-" + str(MAX_LINE) + ")?: ")
        if lines.isdigit():
            lines = int(lines)
            if MAX_LINE >= lines >= 1:
                break
            else:
                print("Please add number greater than 0 or lower than", str(MAX_LINE))
        else:
            print("Invalid amount")
    return lines


def get_bet():
    while True:
        bet_amount = input(f"How much would you like to bet on each line?({MIN_BET}-{MAX_BET}): $")
        if bet_amount.isdigit():
            bet_amount = int(bet_amount)
            if MAX_BET >= bet_amount >= MIN_BET:
                break
            else:
                print(f"Please add value between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Invalid value")
    return bet_amount


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"Not enough to money to bet on that amount")
        else:
            break
    print(f"You are betting ${bet} on {lines}. Total bet is {total_bet}")

    slots = get_slot_machine_spin(Rows, Columns, symbols_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbols_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        elif balance <= 10:
            answer2 = input("You have no money left. Do you want to deposit more?(y or n): ")
            if answer2 == "y":
                balance = deposit()
            elif answer2 == "n":
                break
        balance += spin(balance)
    print(f"You are left with ${balance}")


main()
