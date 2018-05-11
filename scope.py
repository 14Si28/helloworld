n=4
m=10
def exam():
    global n
    print(n)
    print(n+5)
    n+=10

def test():
    print(m)
    print(m+5)
    #m+=10   #Removing '#' will result in error local variable 'm' referenced before assignment
    '''
    this will be resulting in an error as whenever you will try
    to modify the global variable you are supposed to use keyword global,
    however if we want to use them then we can do so.
    '''
exam()
test()