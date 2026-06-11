def get_nums():
    yield 1
    yield 2
    yield 3
    yield 4
    
gen = get_nums()
for i in gen:
    print (i)    