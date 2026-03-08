# Monkey Banana Problem

def monkey_banana(monkey_pos, box_pos, banana_pos):

    print("Initial State")
    print("Monkey position:", monkey_pos)
    print("Box position:", box_pos)
    print("Banana position:", banana_pos)
    print()

    # Step 1: Monkey moves to box
    if monkey_pos != box_pos:
        print("Monkey moves from", monkey_pos, "to", box_pos)
        monkey_pos = box_pos

    # Step 2: Monkey pushes box to banana position
    if box_pos != banana_pos:
        print("Monkey pushes box from", box_pos, "to", banana_pos)
        box_pos = banana_pos
        monkey_pos = banana_pos

    # Step 3: Monkey climbs the box
    print("Monkey climbs onto the box")

    # Step 4: Monkey grabs banana
    print("Monkey grabs the banana")

    print("\nGoal Achieved: Monkey got the banana!")


# Taking input from user
monkey = input("Enter monkey position: ")
box = input("Enter box position: ")
banana = input("Enter banana position: ")

monkey_banana(monkey, box, banana)
