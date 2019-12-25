from __future__ import print_function
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


def geethuParser():
    # sntnce = input('Enter strings')
    n = 4
    sntnce = input('Enter sentence to be parsed:\n')
    wrds = sntnce.split(' ')
    print(wrds)
    rm_list = []
    itm_set = set()
    for i, wrd in enumerate(wrds):
        lttr = list(wrd)
        if lttr[0] == '+':
            lttr.pop(0)
            wrds[i] = ''.join(lttr)
        elif (wrd in itm_set) or len(lttr) < n or lttr[0] == '-':
            rm_list.append(i)
        # elif lttr[0] == '-':
        #     rm_list.append(i)
        # elif len(lttr) < n:
        #     rm_list.append(i)
        # elif wrd in itm_set:
        #     rm_list.append(i)
        # print(wrd in itm_set)
        itm_set.add(wrd)

    for i in reversed(rm_list):
        wrds.pop(i)
    sntnce = ' '.join(wrds)
    print(sntnce)


def takeInput():
    pass


if __name__ == '__main__':
    # letterShift()
    geethuParser()
