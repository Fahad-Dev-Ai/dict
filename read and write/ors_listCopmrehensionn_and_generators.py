def greet(func):
    def main_working():
        print("started")
        func()
        print("ended")
    return main_working
def get_numbers():
    yield 1    
    yield 2
    yield 3    
    yield 4
    yield 5  
    yield 6    
    yield 7    
    yield 8    
    yield 9    
    yield 10    

@greet
def main_work():
    b = get_numbers()
    a = [i for i in b if i%2==0 ]
    print(a)

main_work()
