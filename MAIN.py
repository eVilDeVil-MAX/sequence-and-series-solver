
import math


def an():
    x = a + ((n - 1) * d)
    return x, 'this is the valur of ur term  '


def apsum():
    xsum = ((n/2)*(2*a + ((n-1)*d)))
    
    return xsum, 'this is the sum of ur arithmetic series'


def gn():
    gnth = (an * (r**(ng - 1)))
    return gnth, 'this is the value of ur term   '


def gp_sum():
    g = an * (((r**ng) - 1) / (r - 1))
    return g, 'this is the sum of ur geometric progression'


def infinite_gp_sum():
    inf_gp = an * (1 / (1 - r))
    return inf_gp, 'this is the sum of ur infinite geometric series '


def hn():
    hr = 1/(ah+(nh - 1)*dh)
    return hr, 'this is ur term '


def hp_sum():
    hp = (1 / dh) * math.log((2 * ah + ((2 * nh - 1) * d)) / ((2 * ah) - 1))
    return hp, 'this is the sum of ur hp'

try:

    print('hello welcome to my program on sequence and series ')
    print('chose ur series ')
    print('1.Arthematic progression ')
    print('2.Geometric progression ')
    print('3.harmonic progression ')
    print('4.exit')

    series = int(input('enter ur choice '))

    if series == 1:
        print('what do u want to find in ur AP ')
        print('1. nth term of the ap ')
        print('2.sum of n term of the ap ')
        aa = int(input('enter ur choice:'))
        if aa == 1:
            a = int(input('enter the first term of ur asthmatic progression: '))
            d = int(input('enter the common difference of ur arithmetic progression: '))
            n = int(input('enter the position of the the element u want to find: '))
            print(an())

        elif aa == 2:
            a = int(input('enter the first term of ur arthemaatic progression: '))
            d = int(input('enter the common difference of ur arithmetic progression: '))
            n = int(input('enter the position of the the element till where u want to find its sum: '))
            print(apsum())

        else:
            print('invalid syntax')

    if series == 2:
        print('what do u want to find in ur geometric progression ')
        print('1. i want to find the nth term of my G.p ')
        print('2. i wnat to find the sum of nth term of my G.P')
        print('3. i want to find the sum of infinite term on my G.P')

        G = int(input('what is ur choice: '))

        if G == 1:
            an = int(input('enter the first term of ur Gp: '))
            r = int(input('enter the comman ratio of ur GP: '))
            ng = int(input(' enter the position of ur element '))
            print(gn())

        elif G == 2:
            an = float(input('enter the first term of ur Gp: '))
            r = float(input('enter the comman ratio of ur GP: '))
            ng = float(input(' enter the position of ur element till where u have to find the sum of ur G.p '))
            print(gp_sum())

        elif G == 3:
            an = int(input('enter the first term of ur GP'))
            r = int(input('enter the common ration of ur GP'))
            print(infinite_gp_sum())

        else:
            print('invalid syntax')

    if series == 3:
        print('what do u want to find in ur HP ')
        print('1. nth term of the HP ')
        print('2.sum of n term of the HP ')
        ha = int(input('enter ur choice:'))

        if ha == 1:
            ah = (int(input('enter the first term of ur Hp')))
            dh = (int(input('enter the command difference of ur hp')))
            nh = int(input('enter the position of the element u want to find '))


            print(hn())

        if ha == 2:
            ah = (int(input('enter the first term of ur Hp')))
            dh = (int(input('enter the command difference of ur hp')))
            nh = int(input('enter the position of the element u want to find '))
            
            print(hp_sum())

    if series == 4:
        exit()        

except Exception:
    print('invalid syntax')









