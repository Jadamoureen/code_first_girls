def egg_for_omelette(no_box_of_egg):
    egg_in_box = 6 * no_box_of_egg
    total_egg_needed = egg_in_box//4
    message = 'You can make {} omelettes with {} boxes of eggs'.format(total_egg_needed, no_box_of_egg)
    return message
no_of_egg_box = int(input('How many boxes of eggs do you have? '))
result = egg_for_omelette(no_of_egg_box)
print(result)