
lst = [1, 2, 3, 4]

def get_item(lst):
    for n in lst:
        print("yielding %d" % n)
        yield n


print(get_item(lst))