import random
import os
from time import sleep
from sys import exit


def dead_state(width, height):
    state = []
    for i in range(0, height):
        state.append([" "] * width)
    return state


def random_state(width, height):
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
    top_and_bottom_border = ("-" * len(state[0])) * 2
    
    print(" " + top_and_bottom_border)
    
    for row in state:
        print("| " + " ".join(map(str, row)) + " |")
            
    print(" " + top_and_bottom_border)


def next_board_state(state):
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

            for key in neighbors:
                if neighbors[key] == is_alive:
                    alive += 1
                elif neighbors[key] == is_dead:
                    dead += 1
                elif neighbors[key] == "Z":
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

    
def run_it(state):
    while True:
        new_state = next_board_state(init_state)
        os.system('cls')
        if new_state == next_board_state(new_state):
            render(new_state)
            exit()
        else:
            new_state = next_board_state(new_state)
            render(new_state)
            sleep(1)


first_run = True    
    
while True:
    
    if first_run == True:
        print("Welcome to game_of_life (now with zombies)\n")
        width, height = input("Enter width and height separeted by a comma [10, 10] >> ").split(",")
        first_run == False          
        init_state = random_state(int(width), int(height))
        render(init_state)
        run_it(init_state)
    else:
        cont = input("Would you like to see more?  [y/N] ")
        if not cont.lower().startswith("y"):
            exit()
        else:
            width, height = input("Enter width and height separeted by a comma [10, 10] >> ").split(",")
            init_state = random_state(int(width), int(height))
            render(init_state)
            run_it(init_state)
