import argparse

power_of_two = lambda n: not (n & (n - 1))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-i', 
        help='allows you to enter a number (-i n)',
        type=float
    )
    args = parser.parse_args()    

    info = [
        'Enter the desired number: ',
        '[ERROR]: Input must be a number.',
        'is the exact power of 2.',
        'is not an exact power of 2'
    ]
    n = args.i

    if args.i == None:
        while True:
            try:
                n = float(input(info[0])) 
                break
            except ValueError:
                print(info[1])
        if int(n) == n and n >= 1:
            if power_of_two(int(n)):
                print(int(n), info[2])
            else:
                print(int(n), info[3])
        elif (n > 0 and n < 1 and 1/n == int(1/n)):
            if power_of_two(int(1/n)):
                print(n, info[2])
            else:
                print(n, info[3])
        else:
            print(n, info[3])
    else:
        if int(n) == n and n > 1:
            if power_of_two(int(n)):
                print(int(n), info[2])
            else:
                print(int(n), info[3])
        elif 1/n == int(1/n):
            if power_of_two(int(1/n)):
                print(n, info[2])
            else:
                print(n, info[3])


if __name__ == "__main__":
    main()