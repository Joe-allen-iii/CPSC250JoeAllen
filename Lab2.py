#Lab 2 Labs


# 3.15 LAB: Phone number breakdown

phone_number = int(input())

f1 = phone_number // 10000000

f2 = phone_number % 10000000


f3 = f2 // 10000

f4 = phone_number % 10000

print(f'({f1}) {f3}-{f4}')

# 3.16 LAB: Simple statistics
num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())

floatprod = num1 * num2 * num3 * num4

floatavg = (num1 + num2 + num3 + num4) / 4

intprod = round(floatprod)

intavg = round(floatavg)

print(f'{intprod:.0f} {intavg:.0f}')

print(f'{floatprod:.3f} {floatavg:.3f}')

# 4.15 LAB: Interstate highway numbers
highway_number = int(input())

if 0 < highway_number < 100:
    status = 'primary'
    if highway_number % 2 == 0:
        direct = 'east/west'
    else:
        direct = 'north/south'
    print(f'I-{highway_number} is {status}, going {direct}.')
else:
    status = 'auxiliary'
    if highway_number % 100 == 0:
        print(f'{highway_number} is not a valid interstate highway number.')

    elif highway_number % 2 == 0:
        direct = 'east/west'
        service = highway_number % 100
    else:
        direct = 'north/south'
        service = highway_number % 100

    print(f'I-{highway_number} is {status}, serving I-{service}, going {direct}.')

# 4.18 LAB: Leap year
is_leap_year = False

year = int(input())

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(f'{year} - leap year')
else:
    print(f'{year} - not a leap year')

# 4.19 LAB: Golf scores

par_list = [3, 4, 5]
par = int(input())

score = int(input())

if (par not in par_list) or (score not in range(1, 8)):
    print('Error')

else:
    if par > score:
        if par - score == 2:
            print('Eagle')

        elif par - score == 1:
            print('Birdie')

    elif par < score:

        if score - par == 1:
            print('Bogey')

    else:
        print('Par')


# 5.18 LAB: Brute force equation solver
#This is the first lab I had alot of trouble with and I had to consult stack overflow
# I didnt really understand for awhile, but i took a long break

''' Read in first equation, ax + by = c '''
a = int(input())
b = int(input())
c = int(input())

''' Read in second equation, dx + ey = f '''
d = int(input())
e = int(input())
f = int(input())

solution = False

# test each value of x and y from -10 to 10
for x in range(-10, 11):
    for y in range(-10, 11):

        if ((a * x) + (b * y) == c) and ((d * x) + (e * y) == f):
            print(f'x = {x} , y = {y}')
            solution = True
            break

    if solution:
        break

if not solution:
    print('There is no solution')

# 5.19 LAB: Adjust values in a list by normalizing

bound = int(input())

my_list = []

while len(my_list) < bound:
    my_list.append(input())

float_list = []

for i in my_list:
    float_list.append(float(i))

ss = max(float_list)

for i in float_list:
    value = i / ss
    print(f'{value:.2f}')

# 6.21 LAB: Convert to binary - functions

#I watched the example in class and it made sense and I thought my outputs were correct in pycharm
#I didnt realize what i was doing wrong
def int_to_reverse_binary(x):
    string = ""
    while x > 0:
        num = x % 2
        x = x // 2
        string = string + str(num)
    return string


def string_reverse(string):
    return string[::-1]


if __name__ == '__main__':
    n = int(input())
    answer = int_to_reverse_binary(n)
    answer = string_reverse(answer)
    print(answer)

    # Your code must call int_to_reverse_binary() to get
    # the binary string of an integer in a reverse order.
    # Then call string_reverse() to reverse the string
    # returned from int_to_reverse_binary().


# 6.22 LAB: Swapping variables
# I wasnt sure whether I hardcoded this solution but I passed all the unit tests
def swap_values(user_val1, user_val2, user_val3, user_val4):
    return user_val2, user_val1, user_val4, user_val3


if __name__ == '__main__':
    user_val1 = int(input())
    user_val2 = int(input())
    user_val3 = int(input())
    user_val4 = int(input())

    n_val1, n_val2, n_val3, n_val4 = swap_values(user_val1, user_val2, user_val3, user_val4)

    print(n_val1, n_val2, n_val3, n_val4)


# 6.23 LAB: Fibonacci sequence
def fibonacci(n):
    if n < 0:
        answer = -1
        return answer
    else:
        fiblist = [0, 1]
        for i in range(2, n + 1):
            fiblist.append(fiblist[i - 1] + fiblist[i - 2])
    return fiblist[n]


if __name__ == '__main__':
    start_num = int(input())
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')


