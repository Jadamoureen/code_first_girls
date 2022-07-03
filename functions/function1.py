#Practicing the args and kwargs
#Practice 2

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ['Math', 'Science', 'Arts']
information = {'gender': 'Female', 'age': 20, 'name': 'Moureen'}

""""
when the function is called, the information is displayed
on one line (['Math', 'Science', 'Arts'], {'gender': 'Female', 'age': 20, 'name': 'Moureen'})
followed by an empty dict"""

student_info(courses,information)
