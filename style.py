import sys
import os


def one(): print('one')


def two(): print('two')


def three(): print('three')


def four(): print('four')


def five(a, b, c, d, e): print(a, b, c, d, e)


def throw(): raise Exception('threw')


def oops(): print('oops')


def FindSum(var_one, var_two, var_three,
            var_four):
    s = (var_one +
         var_two +
         var_three +
         var_four)
    return s


def complex(real, imag=0.0):
    return magic(r=real, i=imag)


II = 1
OO = 1
kk = 1
ll = 1

s = FindSum(II, OO,
            kk, ll)

print(s)

A = [1, 2, 3, 4, 5]

print(A[1], {'foo': 2})

x = 1
y = 2

if x == 4:
    print(x, y)
    x, y = y, x

dct = {}
lst = [1, 2, 3, 4]
index = 3
dct['key'] = lst[index]

x = 1
y = 2
long_variable = 3

i = 0
i = i+1

submitted = 0
submitted += 1

x = x * 2 - 1
hypot2 = x * x + y * y
x = (x + y) * (x - y)

foo = 'blah'
if foo == 'blah':
    one()
two()
three()
four()

foo = 'non_blah'
if foo == 'blah':
    four()
else:
    one()

try:
    throw()
except Exception:
    oops()
finally:
    one()

one()
two()
five(II, OO, kk,
     ll, x)

if foo == 'blah':
    one()
    two()
    three()
