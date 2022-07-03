#Practicing the args and kwargs
#Practice 3

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ['Math', 'Science', 'Arts']
information = {'gender': 'Female', 'age': 20, 'name': 'Moureen'}

""""
when the function is called with specific asterisks,
There is a TypeError
TypeError: student_info() argument after ** must be a mapping, not list"""

student_info(*information,**courses)
