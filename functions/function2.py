#Practicing the args and kwargs
#Practice 3

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ['Math', 'Science', 'Arts']
information = {'gender': 'Female', 'age': 20, 'name': 'Moureen'}

""""
when the function is called with specific asterisks, the information is displayed
('Math', 'Science', 'Arts')
{'gender': 'Female', 'age': 20, 'name': 'Moureen'}"""

student_info(*courses,**information)
