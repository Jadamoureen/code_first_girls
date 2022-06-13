"""
I have a lot of boxes of eggs in my fridge and I want to calculate how many omelettes I can make. Write a program to calculate this.
Assume that a box of eggs contains six eggs and I need four eggs for each omelette, but I should be able to easily change these values if I want. The output should say something like:
"""

while True:

    #take input from the user
    boxes_of_eggs = int(input("Enter choice(6/9/18): "))

    #check if choice is in one of the four choices
    if boxes_of_eggs in (6,9,18):
        total_boxes = 6 * boxes_of_eggs//4
        print('You can make {} omelettes with {} boxes of eggs'.format(total_boxes, boxes_of_eggs))

        break

    else:
        print("Invald Input")
