"""
I have a lot of boxes of eggs in my fridge and I want to calculate how many omelettes I can make. Write a program to calculate this.
Assume that a box of eggs contains six eggs and I need four eggs for each omelette, but I should be able to easily change these values if I want. The output should say something like:
"""

while True:

    #take input from the user
    boxes_of_eggs = int(input("Enter the number of boxes of eggs: "))

    #calculates the number of omelettes
    if boxes_of_eggs:
        total_boxes = 6 * boxes_of_eggs//4
        print('You can make {} omelettes with {} boxes of eggs'.format(total_boxes, boxes_of_eggs))

    break
else:
        print("Invald Input")
