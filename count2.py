with open('my_file.txt') as fh:
	text = fh.read()
count = 0
for i in text:
    if i.isupper():
        count += 1
        
print(count)