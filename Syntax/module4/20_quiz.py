count = 0

def show_count():
    print(f"count = {count}")


def set_count(c):
    global count
    count = c

def set_count2(c,c2):
    print(id(c))
    print(id(c2))
    c=c2
    print(id(c))
    print(id(c2))

show_count()
set_count(7)
show_count()

set_count2(5,6)