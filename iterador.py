from decorators import execution_time

my_list = [1,2,3,4,5]
my_iter = iter(range(1,1000000))

@execution_time
def iterando():
    while True:
        try:
            element = next(my_iter)
            print(element)
        except StopIteration:
            break

iterando()