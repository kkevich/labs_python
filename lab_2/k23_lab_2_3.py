import os
import argparse


def delete(names):
    total = len(names)
    current = 1
    for name in names:
        os.remove(name)
        progress('deleting files:', total, current)
        print()


def renametxt(name, new):
    """ Function renames the sorted file. 
        If the name of such file exists, 
        then the function will rename file 
        until such a name exists.

        return: None
    """
    lgth = len(new)
    counter = 0 
    while True:
        if os.path.isfile(new + '.txt'):
            counter += 1
            new = new[:lgth] + str(counter)
        else:
            os.rename(name, new + '.txt')
            break


def progress(txt, total, current):
    print('\r{} [{}/{}]'.format(txt, current, total), end='')


def sort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 
        L = arr[:mid] 
        R = arr[mid:] 
        sort(L) 
        sort(R) 
        i = j = k = 0      
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1


def split(file, size):
    """ The function reads the main file in chunks, 
        then sorts and writes these chunks to separate files.  

        return: list with names of sorted files
    """ 
    piece = os.path.getsize(file)
    total = int(piece/size) # number of files 
    names = []
    with open(file, 'r') as f:
        counter = 0
        while True:
            # 25mb chunk 
            text = f.readlines(size)
            progress('splitting files:', total, len(names))
            if len(text) == 0:
                break

            # sorting each string
            first_words = [None] * len(text) 
            tmp = list(map(lambda line: line.rstrip().split(), text))
            for id, line in enumerate(tmp):
                sort(line)
                first_words[id] = line[0]
                tmp[id] = ' '.join(line) + '\n'

            # sorting all strings
            idx = range(len(first_words))
            word_idx = list(zip(first_words, idx))
            sort(word_idx)
            idx_sorted = (i[1] for i in word_idx)

            # writing a chunk to a file
            name = 'tmp_' + str(counter)
            chunk = open(name, 'w')
            for i in idx_sorted:
                chunk.write(tmp[i])
            chunk.close()

            tmp.clear()
            text.clear()
            counter += 1
            names.append(name)
        print()
    return names


def merge(names):
    """ The function reads two chunks in a loop 
        and sorts them into one file.

        srt: List where sorted and merged files 
        will be stored.

        return: File list. 
        In the last place of the list is the final file.
    """ 
    srt = []
    srt.append(names[-1])
    total = len(names[:-1])
    current = 0
    for name in names[:-1]:
        progress('merging files:', total, current)
        new_name = 'srt_' + name[4:]
        new = open(new_name, 'w')
        with open(name, 'r') as f1, open(srt[-1], 'r') as f2:
            f1_line = f1.readline()
            f2_line = f2.readline()   
            while f1_line and f2_line:
                if f1_line.split(' ')[0] < f2_line.split(' ')[0]:
                    new.write(f1_line)
                    f1_line = f1.readline()
                else:
                    new.write(f2_line)
                    f2_line = f2.readline()
            while f1_line:
                new.write(f1_line)
                f1_line = f1.readline()
            while f2_line:
                new.write(f2_line)
                f2_line = f2.readline()

        # deleting temporary chunk
        os.remove(name)
        
        srt.append(new_name)
        current += 1
        new.close()
    progress('merging files:', total, current)
    del names
    print()
    return srt


def main():
    chunk = 26214400

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-i',
        help='set input file (-i file_name.txt)',
    )
    parser.add_argument(
        '-o',
        help='set output fle (-o file_name.txt)'
    )
    args = parser.parse_args()
    file = args.i
    output = args.o

    names = split(file, chunk)
    srt = merge(names)
    delete(srt[:-1])
    renametxt(srt[-1], output)

    print('\nSORTING DONE\n')
    input()


if __name__ == "__main__":
    main()
