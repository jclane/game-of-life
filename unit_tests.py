from life import next_board_state
from life import render

# TODO: there's a lot of repeated code here. Can
# you move some of into reusable functions to
# make it shorter and neater?

def test(test_num, init_state, expected_next_state, actual_next_state):
    if expected_next_state == actual_next_state:
        print("PASSED", test_num)
    else:
        print("FAILED {}!".format(test_num))
        print("Expected:")
        render(expected_next_state)
        print("Actual:")
        render(actual_next_state)

if __name__ == "__main__":
    # TEST 1: dead cells with no live neighbors
    # should stay dead.

    init_state1 = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    expected_next_state1 = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    actual_next_state1 = next_board_state(init_state1)
    
    test("1", init_state1, expected_next_state1, actual_next_state1)

    # TEST 2: dead cells with exactly 3 neighbors
    # should come alive.
    init_state2 = [
        [0,0,1],
        [0,1,1],
        [0,0,0]
    ]
    expected_next_state2 = [
        [0,1,1],
        [0,1,1],
        [0,0,0]
    ]
    actual_next_state2 = next_board_state(init_state2)

    test("2", init_state2, expected_next_state2, actual_next_state2)
    
    # TEST 3: live cells wih more thn 3 live neighbors
    # should die

    init_state3 = [
        [1,1,1],
        [0,1,1],
        [0,0,0]
    ]
    expected_next_state3 = [
        [1,0,1],
        [0,0,1],
        [0,0,0]
    ]
    actual_next_state3 = next_board_state(init_state3)

    test("3", init_state3, expected_next_state3, actual_next_state3)
    
    # TEST 4: cells on the edges of the board behave 
    # as expected

    init_state4 = [
        [1,1,1],
        [1,0,1],
        [1,1,1]
    ]
    expected_next_state4 = [
        [1,0,1],
        [0,0,0],
        [1,0,1]
    ]
    actual_next_state4 = next_board_state(init_state4)

    test("4", init_state4, expected_next_state4, actual_next_state4)
    
    # TEST 5: dead cells in corners should come alive
    # if neighbored by 3 live cells

    init_state5 = [
        [0,1,0],
        [1,1,0],
        [0,0,0]
    ]
    expected_next_state5 = [
        [1,1,0],
        [1,1,0],
        [0,0,0]
    ]
    actual_next_state5 = next_board_state(init_state5)

    test("5", init_state5, expected_next_state5, actual_next_state5)
