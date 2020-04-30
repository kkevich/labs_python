
# pre-calculated array blocks
def subsums(lst, lgth):
    subsum = 0
    total = []
    for i in range(1, len(lst) + 1):
        subsum += lst[i-1]
        if i % lgth == 0:
            total.append(subsum)
            subsum = 0
    if subsum != 0:
        total.append(subsum)
    return total


# sum to the right end
def rsum(lst, lgth, r):
    total = 0
    i = 0
    while i + lgth <= r and i % lgth == 0:
        total += subsums(lst, lgth)[i // lgth]
        i += lgth
    for i in range(i, r):
        total += lst[i]
    return total


# sum on the segment from left end to the right
def segsum(lst, lgth, l, r):
    if l == 0:
        return rsum(lst, lgth, r)
    else:
        return rsum(lst, lgth, r) - rsum(lst, lgth, l-1)


# Request for yes or no
def yes_no(question, default=None):
    valid = {"yes": True, "y": True,
            "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        print(question + prompt, end=' ')
        choice = input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            print("Please respond with 'yes'/'no' "
                            "(or 'y'/'n').\n")


def menu():
    print('Choose the option:')
    print(' [1] - Use data from file')
    print(' [2] - Console input')
    print(' ----------------------')
    print(' [0] - Exit\n')

    while True:
        try:
            choice = int(input('Enter number of option: '))
            if choice in (1,2,0):
                break
            else:
                print("Please respond with '1'/'2' or '0'.\n")
        except ValueError:
            print("Please respond with '1'/'2' or '0'.\n")

    if choice == 1:
        yn = yes_no('Are you sure about your choice?', 
                    default='yes')
        if yn == True:
            f = open('exx.txt', 'r')
            print('\nLists from file:')
            lines = f.readlines()
            idx = 1
            for i in lines:
                print(' [{0}] -'.format(idx), eval(i))
                idx += 1
            f.close()
            print('\nWhich list would you use?')

            while True:
                try:
                    pick = int(input('Enter list number: '))
                    if pick in range(1, len(lines)+1):
                        break
                    else:
                        print('Please write correctly list number.\n')
                except ValueError:
                    print("Please write correctly list number.\n")
            lst = eval(lines[pick - 1])
            print('List:', lst)
            lgth = int(len(lst)**0.5 + 1)
            length = len(lst)

            print('\nQuery:')
            print('The sum on the segment of the array from [l] to [r]\n')

            print('Query execution:')
            while True:
                try:
                    l = int(input('Enter [l] from the range of {}: '.format(length)))
                    r = int(input('Enter [r] from the range of {}: '.format(length)))
                    total = segsum(lst, lgth, l, r)
                    break
                except IndexError:
                    print('\nList index out of range.')
                except ValueError:
                    print('\nPlease write correctly number.')
            print('The sum from [{}] to [{}] is {}.\n'.format(l, r, total))

            print('Request completed successfully.')
        else:
            print()
            menu()

    if choice == 2:
        yn = yes_no('Are you sure about your choice?', 
                    default='yes')
        if yn == True:
            string = input('\nEnter numbers in list separated by spaces: ')
            lst = str_to_lst(string)
            lgth = int(len(lst)**0.5 + 1)
            length = len(lst)
            print('List of numbers: ', lst, '\n')

            print('Query:')
            print('The sum on the segment of the array from [l] to [r]\n')

            print('Query execution:')
            while True:
                try:
                    l = int(input('Enter [l] from the range of {}: '.format(length)))
                    r = int(input('Enter [r] from the range of {}: '.format(length)))
                    total = segsum(lst, lgth, l, r)
                    break
                except IndexError:
                    print('\nList index out of range.')
                except ValueError:
                    print('\nPlease write correctly number.')
            print('The sum from [{}] to [{}] is {}.\n'.format(l, r, total))
            print('Request completed successfully.')
        else:
            print()
            menu()
    
    if choice == 0:
        exit()


# Convert string to list of numbers
def str_to_lst(string):
    try:
        string = string.split()
        numbers = []
        for i in string:
            digit = list(filter(str.isdigit, i))
            digit = ''.join(digit)
            numbers.append(int(digit))
        return numbers  
    except ValueError:
        None


menu()
