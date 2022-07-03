#Practicing the args and kwargs
#Practice 1

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

""""
when the function is called, the information is displayed
('Math', 'Science', 'Arts')
{'gender': 'Female', 'age': 20, 'name': 'Moureen'}"""

student_info('Math','Science','Arts',name='Moureen',age=20,gender='Female')
