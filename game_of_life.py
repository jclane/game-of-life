import random
import os
import csv
from os import path
from time import sleep
from sys import exit


def dead_state(width, height):
    """
    Create board filled with dead cells.

    :param width: integer indicating width to make the board
    :param height: integer indicating height to make the board
    :return: Board sized width*height filled with dead cells.
    """

    state = []
    for i in range(0, height):
        state.append([" "] * width)
    return state


def random_state(width, height):
    """
    Creates a dead_state board and then
    randomly populates that board with
    live cells.

    :param width: integer indicating width to make the board
    :param height: integer indicating height to make the board
    :return: Board sized width*height randomly filled with
        dead/live cells
    """

    state = dead_state(width, height)
        
    for row in state:
        for cell in range(0, len(row)):
            random_num = random.random()
            if random_num >= 0.5:
                row[cell] = "O"
            else:
                row[cell] = " "

    return state
            
            
def render(state):
    """
    Pretty prints the board.

    :param state: list representing board to be printed
    :return: visually appealing output of current board
    """

    top_and_bottom_border = ("-" * len(state[0])) * 2
    
    print(" " + top_and_bottom_border)
    
    for row in state:
        print("| " + " ".join(map(str, row)) + " |")
            
    print(" " + top_and_bottom_border)


def next_board_state(state):
    """
    Use previous board state to generate next state.

    :param state: list as current state of board
    :return: new board
    """

    is_alive = "O"
    is_dead = " " 
    next_state = dead_state(len(state), len(state[0]))

    for row in range(0, len(state)):
        for cell in range(0, len(state[row])):
            cell_state = state[row][cell]
            alive = 0
            dead = 0
            zombie = False

            neighbors = {
                "above": 3,
                "above_left": 3,
                "above_right": 3,
                "below": 3,
                "below_left": 3,
                "below_right": 3,
                "right": 3,
                "left": 3
            }

            try:
                for neighbor in neighbors:
                    if neighbor == "above":
                        neighbors[neighbor] = state[row + 1][cell + 1]
                    if neighbor == "above_left":
                        neighbors[neighbor] = state[row - 1][cell + 1]
                    if neighbor == "above_right":
                        neighbors[neighbor] = state[row - 1][cell]
                    if neighbor == "below":
                        neighbors[neighbor] = state[row - 1][cell - 1]
                    if neighbor == "below_left":
                        neighbors[neighbor] = state[row + 1][cell]
                    if neighbor == "below_right":
                        neighbors[neighbor] = state[row + 1][cell - 1]
                    if neighbor == "right":
                        neighbors[neighbor] = state[row][cell - 1]
                    if neighbor == "left":
                        neighbors[neighbor] = state[row][cell + 1]
            except IndexError:
                pass
                continue

            for neighbor in neighbors:
                if neighbors[neighbor] == is_alive:
                    alive += 1
                elif neighbors[neighbor] == is_dead:
                    dead += 1
                elif neighbors[neighbor] == "Z":
                    zombie = True

            if zombie and alive < 2:
                next_state[row][cell] = "Z"
            else:

                if cell_state == is_alive:
                    if alive <= 1 or alive > 3:
                        next_state[row][cell] = is_dead

                    if alive in range(2, 4):
                        next_state[row][cell] = is_alive

                else:
                    if alive == 3:
                        next_state[row][cell] = is_alive
                    else:
                        random_num = random.random()
                        if random_num >= 0.8:
                            next_state[row][cell] = "Z"
                        else:
                            next_state[row][cell] = is_dead

    return next_state


def save_state(state):
    """
    Save state to text file.

    :param state: state as list to be save
    """

    file = "saved_boards.csv"

    name = input("Enter a name save as >> ")

    if path.exists(file):
        with open(file, "a", newline="") as csvfile:
            writer = csv.writer(csvfile, delimiter="/", quotechar="'")
            to_write = list((",".join(row) for row in state))
            to_write.insert(0, name)
            writer.writerow(to_write)
    else:
        with open("saved_boards.csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile, delimiter="/", quotechar="'")
            to_write = list((",".join(row) for row in state))
            to_write.insert(0, name)
            writer.writerow(to_write)


def load_state():
    """
    Load state from text file.

    :return: load chosen state from text file
    """

    file = "saved_boards.csv"

    if path.exists(file):
        saved_states_dict = {}

        with open(file, "r", newline="") as csvfile:
            reader = csv.reader(csvfile, delimiter="/", quotechar="'")
            saved_states = (row for row in reader)
            for state in saved_states:
                state_name = state[0]
                state_board = []
                for row in state[1:]:
                    row = row.split(",")
                    state_board.append(row)
                print(state_name)
                render(state_board)
                saved_states_dict[state_name] = state_board

            choice = input("Enter the name of the saved state you wish to load >> ")

            init_state = saved_states_dict[choice]
            render(init_state)
            run_it(init_state)


def run_it(state):
    """
    Continuously generate new boards with
    live/dead/zombie cells.

    If new_state is the same as the next
    state the loop will exit else it will
    continue.

    :param state: list as initial state of
        the board
    """

    while True:
        new_state = next_board_state(state)
        os.system('cls')
        if new_state == next_board_state(state):
            render(new_state)
            exit()
        else:
            new_state = next_board_state(state)
            render(new_state)
            sleep(1)


def print_menu():
    """
    Prints the menu.

    :return: Visually appealing output of menu items.
    """

    MENU = {1: "New",
            2: "Load",
            3: "Quit"
    }

    print("Welcome to game_of_life (now with zombies)\n")
    for num in range(1, len(MENU) + 1):
        print("{}. {}".format(str(num), MENU[num]))

    choice = input("What would you like to do? [1-{}] >> ".format(len(MENU) + 1))

    if choice == "1":
        width, height = input("Enter width and height separated by a comma [10, 10] >> ").split(",")
        init_state = random_state(int(width), int(height))
        render(init_state)
        save = input("Would you like to save this start state? [y/N]")
        if save.lower().startswith("y"):
            save_state(init_state)
            run_it(init_state)
        else:
            run_it(init_state)
    if choice == "2":
        load_state()
    if choice == "3":
        exit()


while True:

    print_menu()
