import argparse
from ast import literal_eval


def flatten(sequence):
    for i in sequence:
        if not isinstance(i, str) and hasattr(i, '__iter__'):
            yield from flatten(i)
        else:
            yield(i)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-i',
        help = 'enter any sequence of elements with quotation marks (-i "...")'
    )
    args = parser.parse_args()
    seq = literal_eval(args.i)
    print(list(flatten(seq)))


if __name__ == "__main__":
    main()    
