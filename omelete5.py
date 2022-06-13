while True:

#take input from the user
    boxes_of_eggs = int(input("Enter the number of boxes: "))

    if boxes_of_eggs:
        total_boxes  = 6 * boxes_of_eggs//4
        print('You can make {} omelettes with {} boxes of eggs'.format(total_boxes,boxes_of_eggs))
    break
