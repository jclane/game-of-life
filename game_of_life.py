import random


def dead_state(width, height):
    state = []
    for i in range(0,height):
        state.append([0] * width)
    return state


def random_state(width, height):
    state = dead_state(width, height)
        
    for row in state:
        for cell in range(0, len(row)):
            random_num = random.random()
            if random_num >= 0.5:
                row[cell] = 1
            else:
                row[cell] = 0
        
        next_state.append(state[row])
        
    return next_state
            
            
def render(state):
    top_and_bottom_border = ("-" * len(state[0])) * 2
    
    print(" " + top_and_bottom_border)
    
    for row in state:
        print("| " + " ".join(map(str, row)) + " |")
            
    print(" " + top_and_bottom_border)


def next_board_state(state):
    next_state = []
    
    for row in range(0, len(state)):
        next_state.append([])
        for cell in range(0, len(state[row])):
            alive = 0
            dead = 0
            cell_state = state[row][cell]
            
            above = 3
            above_left = 3
            above_right = 3
            below = 3
            below_left = 3
            below_right = 3
            right = 3
            left = 3
            
            if row != len(state) - 1 and cell != len(state[row]) - 1:
                below_right = state[row + 1][cell + 1]
            
            if row != 0 and cell != len(state[row]) - 1:
                above_right = state[row - 1][cell + 1]
                
            if row != 0:
                above = state[row - 1][cell]
                above_left = state[row - 1][cell - 1]

            if row != len(state) - 1:
                below = state[row + 1][cell]
                below_left = state[row + 1][cell - 1]
                
            if cell != 0:
                left = state[row][cell - 1]
            
            if cell != len(state[row]) - 1:
                right = state[row][cell + 1]
                        
            if left == 1:
                alive += 1
            elif left == 0:
                dead += 1
                
            if right == 1: 
                alive += 1
            elif right == 0:
                dead += 1
                                
            if above == 1:
                alive += 1
            elif above == 0:
                dead += 1
                                
            if below == 1:
                alive += 1
            elif below == 0:
                dead += 1
                
            if below_left == 1:
                alive += 1
            elif below_left == 0:
                dead += 1
            
            if below_right == 1:
                alive += 1
            elif below_right == 0:
                dead += 1
                
            if above_left == 1:
                alive += 1
            elif above_left == 0:
                dead += 1
                
            if above_right == 1:
                alive += 1
            elif above_right == 0:
                dead += 1
                
            if cell_state:
                if alive <= 1 or alive > 3:
                    next_state[row].append(0)
                
                if alive in range(2,4):
                    next_state[row].append(1)

            else:
                if alive == 3:
                    next_state[row].append(1)   
                else:
                    next_state[row].append(0)
        
    return next_state
    
