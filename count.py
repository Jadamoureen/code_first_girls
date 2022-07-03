letters = set()
with open('demo.txt') as countletter:
    count = 0
    text = countletter.read()
    for character in text:
        if character.isupper():
            count += 1
            letters.add(character)
print(count)

