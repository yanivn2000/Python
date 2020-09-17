def lower_first(str):
    lower = []
    other = []
    for char in str:
        if char.islower():
            lower.append(char)
        else:
            other.append(char)
    res = ''.join(lower + other)
    print(res)


def main():
    str = input("Insert a string: ")
    lower_first(str)

if __name__ == '__main__':
    main()

