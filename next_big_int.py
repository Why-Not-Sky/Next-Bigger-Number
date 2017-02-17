import unittest


class NextBigIntegerTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_has_next_big(self):
        self.assertEquals(next_big(1234), 1243)
        self.assertEquals(next_big(1243), 1324)
        self.assertEquals(next_big(1324), 1342)
        self.assertEquals(next_big(1342), 1423)
        self.assertEquals(next_big(1423), 1432)

        self.assertEquals(next_big(1432), 2134)
        self.assertEquals(next_big(2134), 2143)
        self.assertEquals(next_big(2143), 2314)
        self.assertEquals(next_big(2314), 2341)
        self.assertEquals(next_big(2341), 2413)
        self.assertEquals(next_big(2413), 2431)

        self.assertEquals(next_big(2431), 3124)
        self.assertEquals(next_big(3124), 3142)
        self.assertEquals(next_big(3142), 3214)
        self.assertEquals(next_big(3214), 3241)
        self.assertEquals(next_big(3241), 3412)
        self.assertEquals(next_big(3412), 3421)

        self.assertEquals(next_big(3421), 4123)
        self.assertEquals(next_big(4123), 4132)
        self.assertEquals(next_big(4132), 4213)
        self.assertEquals(next_big(4213), 4231)
        self.assertEquals(next_big(4231), 4312)
        self.assertEquals(next_big(4312), 4321)

        self.assertEquals(next_big(3433), 4333)

    def test_no_next_big(self):
        self.assertEquals(next_big(-1), 0)
        self.assertEquals(next_big(1), -1)
        self.assertEquals(next_big(1111), -1)
        self.assertEquals(next_big(4321), -1)

def to_char_list(number):
    return list(map(int, str(number)))

def to_int(numList):
    s = ''.join(map(str, numList))
    return int(s)

def concatenate_int(numOne, numTwo):
    return int(str(numOne)+str(numTwo))

def get_next_int(numList, num):
    numList.sort()
    for val in numList:
        if (val > num): return val

def next_big(number):
    if number < 0: return 0

    to_array = to_char_list(number)
    #reverse_int = to_array[::-1]
    cnt = len(to_array)

    if (cnt == 1) :
        return -1
    else:
        firstOne = to_array[0]
        afterOne = to_array[1:]
        nb = next_big(to_int(afterOne))

        if (nb != -1) : # has next bigger integer
            return concatenate_int(firstOne, nb)
        else: # if none, the next big = the next bigger decimal in (1:) + minimum(remains)
            firstInt = get_next_int(afterOne, firstOne) # get the next bigger int from the list
            # return None if ther are noone greater then it.  111, or 4321
            if firstInt is None: return (-1)

            afterOne.remove(firstInt)
            if afterOne is not None:
                afterOne.append(firstOne)
                afterOne.sort()
            else:
                afterOne = list(firstOne)

            afterOne.insert(0, firstInt)
            return (to_int(afterOne))

def test_big_int():
    print (1, next_big(1))
    print (11, next_big(11))
    print (12, next_big(12))
    print (121, next_big(121))
    print (1234, next_big(1234))

def test_utility():
    number = 23141
    to_array = to_char_list(number)
    print(to_array)
    print(to_int(to_array))

    print (get_next_int(to_array, 2))

def main():
    #test_utility()

    test_big_int()

    return

    tcase = NextBigIntegerTestCase()
    tcase.test_has_next_big()
    tcase.test_no_next_big()

if __name__ == '__main__':
    main()