import random
import string
import argparse
import time

alphabet = string.ascii_letters


def progress(txt, total, current):
    p = int(100 * current/total)
    print('\r{} {}%'.format(txt, p), end='')


def word_generator(l):
    L = random.choice(range(*l))
    word = ''
    for letter in range(L):
        word = word + random.choice(alphabet)
    return word


def string_generator(k, l):
    K = random.choice(range(*k))
    string = ''
    for word in range(K):
        string = string + word_generator(l) + ' '    
    return string[:-1] + '\n'
        

def last_word(l):
    return ''.join(random.choice(alphabet) for x in range(l))


def last_string(l, dif, max_in_word):
    string = ''
    word = ''
    i = 0
    while i < (dif - max_in_word):
        word = word_generator(l)
        string += word + ' '
        i += len(word + ' ')
    return string + last_word(dif - i)


def file_generator(name, size, k=(10, 100), l=(3, 10)):
    mb = round(size*1048576)

    with open(name + '.txt', 'w+') as f: 
        max_in_row = l[1] * k[1]
        max_in_word = l[1]

        while f.tell() < mb - max_in_row:
            progress('creating file: ', mb, f.tell())
            f.write(string_generator(k, l))
        dif = mb - f.tell()
        progress('creating file: ', mb, f.tell())
        f.write(last_string(l, dif, max_in_word)) 
        progress('creating file: ', mb, f.tell())


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-n',
        '--name',
        help="enter the name of file (-n NAME)",
        type=str
    )
    parser.add_argument(
        '-s',
        '--size',
        help='allows you to enter the file size in megabytes(-s SIZE)',
        type=float
    )
    parser.add_argument(
        '-k',
        help='number of words per line in the range from A to B (-k A B))',
        type=int,
        nargs='*'
    )
    parser.add_argument(
        '-l',
        help='length of each word in the range from A to B (-l A B))',
        type=int,
        nargs='*'
    )
    args = parser.parse_args()

    name = args.name
    size = args.size
    if args.k == None:
         k = (10, 100)
    else: 
        k = tuple(args.k)
    if args.l == None:
        l = (3, 10)
    else: 
        l = tuple(args.l)

    file_generator(name, size, k, l)
    

if __name__ == "__main__":
    main()
