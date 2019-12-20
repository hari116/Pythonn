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
    pass


def takeInput():
    pass


if __name__ == '__main__':
    letterShift()