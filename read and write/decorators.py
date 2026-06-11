def fundamental_greet(func):
    def wrapper(*args):
        print("Function started")
        func(*args)
        print("function ended") 
    return wrapper

@fundamental_greet
def calculator(a,b):
    print(a+b)

calculator(67,69)