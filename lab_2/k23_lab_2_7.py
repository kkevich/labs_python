import argparse


def leonardo():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b + 1
gen = leonardo()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-i', 
        help='allows you to enter a number (-i n)',
        type=int 
    )
    args = parser.parse_args()
    
    info = [
        'Enter a number to determine the n-th Leonardo number: ',
        'The n-th Leonardo number:',
        '[ERROR]: Input must be positive integer.',
        ]
    n = args.i

    if args.i == None:
        while True:
            try:
                n = int(input(info[0]))
                if n >= 0:
                    break
                else:
                    print(info[2])
            except ValueError:
                print(info[2])
        for i in range(n-1):
            next(gen)
        print(info[1], next(gen))
    elif args.i >= 0:
        for i in range(n-1):
            next(gen)
        print(info[1], next(gen))
    else:
        print(info[2])


if __name__ == "__main__":
    main()
