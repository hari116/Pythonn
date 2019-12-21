from sys import argv as argv


# move specified character to the offset given (adarsh s quest)
def actualLetterShift(word, pos, off):
    myList = list(word)
    pos -= 1  # array pos
    final_pos = pos + off  # given pos + off -1
    for i in range(pos, final_pos):
        tmp = myList[i]
        myList[i] = myList[i + 1]
        myList[i + 1] = tmp
    word = ''.join(myList)
    return word


def letterShift():
    print(argv)
    if argv:
        strng, pos, offst = argv[1:]
    else:
        inpt = input('Enter word, position and order[Seperate by spaces]:\n')
        strng, pos, offst = inpt.split(' ')
    pos = int(pos)
    offst = int(offst)
    if pos + offst <= len(strng):
        print(actualLetterShift(strng, pos, offst))
    else:
        print('Invalid input!')


def parser():
    str = 'take an input an +add -inus again'
    n = 4
    wrds = str.split(' ')
    print(wrds)
    rm_list = []
    # for i in range(0, len(wrds)):
    for i in range(len(wrds) - 1, -1, -1):
        lttr = list(wrds[i])
        # print(wrds[i])
        if lttr[0] == '+':
            lttr.pop(0)
            wrds[i] = ''.join(lttr)
        elif lttr[0] == '-':
            rm_list.append(i)
        else:
            if len(lttr) < n:
                rm_list.append(i)
        nw_wrd = ''.join(lttr)
        # print(nw_wrd)
        print(rm_list)
    for i in rm_list:
        wrds.pop(i)
    print(wrds)

def takeInput():
    pass


if __name__ == '__main__':
    # letterShift()
    parser()
