def my_country(country="Rwanda"):
    print(f"Hello from {country}")

def greet(*names):
    for name in names:
        print(f"Hello {name}")

def sum(*numbers):
    answer=0
    for num in numbers:
        answer+=num
        return answer

def multiply(*numbers):
        answer=1
        for number in numbers:
            answer*=number
        return answer

def student_attributes(**kwargs):
     for key,value in kwargs.items():
        print(f"{key}:{value}")

#A function named concatenate_args that takes any number of string arguments in 
#positional arguments format and concatenates them into a single string.

def concatenate_args(*number):
        answer=" "
        for num in number:
            answer+=num
        return answer

#A function named concatenate_kwargs that takes any number of string arguments in 
#keyword arguments  format and concatenates them into a single string.

def concatenate_kwargs(**kwargs):
    answer=" "
    for key,value in kwargs.items():
        answer+=value
    return answer
        

























































