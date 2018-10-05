import random
import os
from time import sleep


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
    next_state = []

    def set_cell_state(row, cell):
        cell_state = state[row][cell]

        if zombie and alive < 2:
            next_state[row].append("Z")
        else:

            if cell_state == is_alive:
                if alive <= 1 or alive > 3:
                    next_state[row].append(is_dead)

                if alive in range(2, 4):
                    next_state[row].append(is_alive)

            else:
                if alive == 3:
                    next_state[row].append(is_alive)
                else:
                    random_num = random.random()
                    if random_num >= 0.8:
                        next_state[row].append("Z")
                    else:
                        next_state[row].append(is_dead)

    for row in range(0, len(state)):
        next_state.append([])
        for cell in range(0, len(state[row])):
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

            set_cell_state(row, cell)

    return next_state


init_state = random_state(3, 3)
render(init_state)
new_state = next_board_state(init_state)


while True:
    os.system('cls')
    if new_state == next_board_state(new_state):
        render(new_state)
        break
    else:
        new_state = next_board_state(new_state)
        render(new_state)
        sleep(1)
