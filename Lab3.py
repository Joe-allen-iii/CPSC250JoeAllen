#Lab 3

# 7.5 LAB: Checker for integer string
user_string = input()

if user_string.isalnum():
    print('Yes')

else:
    print('No')

# 7.6 LAB: Name format
name = input().split()

if len(name) == 3:

    first_initial = name[0][0]

    mid_initial = name[1][0]

    last_name = name[2]
    print(f'{last_name}, {first_initial}.{mid_initial}.')

else:
    first_initial = name[0][0]

    last_name = name[1]

    print(f'{last_name}, {first_initial}.')

#7.7 LAB: Count characters
#I didnt really understand how to get the output as desired so I tried looking back into the book

#Im not sure if i coded it as anticipated

dinput = input().split()

dtarget = dinput[0]

dphrase = ' '.join(dinput[1:])

count = dphrase.count(dtarget)

if count == 1:
    print(count, dtarget)

else:

    print(f'{count} {dtarget}\'s')

# 7.8 LAB: Mad Lib - loops


madlib = input().split()
num = madlib[1]
madlib = ' '.join(madlib[0:1])

while 'quit' not in madlib:
    print(f'Eating {num} {madlib} a day keeps you happy and healthy.')
    madlib = input().split()
    num = madlib[1]
    madlib = ' '.join(madlib[0:1])


# 7.9 LAB: Palindrome

OG = input()
word = OG.replace(" ", "")

mylist = list(word)
mylist.reverse()
reverseword = "".join(mylist).replace(" ", "")

if word == reverseword:
    print('palindrome:', OG)

else:
    print('not a palindrome:', OG)

# 8.16 LAB: Varied amount of input data

my_list = input().split()

my_list = [float(i) for i in my_list]

max_ = max(my_list)

sum_ = sum(my_list)

n = len(my_list)

avg = sum_ / n

print(f'{max_:.2f} {avg:.2f}')

# 8.17 LAB: Filter and sort a list
#it took me a bit to realize my problems with the list comprehension
#I had to go back in the book
my_list = [int(i) for i in input().split()]

neglist = [int(i) for i in my_list if i < 0]

neglist.sort()

neglist.reverse()

for i in neglist:
    print(i, end = " ")
# nonneg = [i for i in my_list if i < 0]
# print(nonneg)


# 8.18 LAB: Elements in a range

my_list = [int(i) for i in input().split()]

bounds = [int(i) for i in input().split()]

ret = [int(i) for i in my_list if min(bounds) <= i <= max(bounds)]


for i in ret:
    print(i , end = ",")


# 8.19 LAB: Contact list
contact_list = input()
pairs = contact_list.split()

contacts = {}
for pair in pairs:
    name, phone_number = pair.split(',')
    contacts[name] = phone_number

search_name = input()

phone_number = contacts[search_name]
print(phone_number)

# 8.20 LAB: Car wash

services = {
    'Air freshener': 1,
    'Rain repellent': 2,
    'Tire shine': 2,
    'Wax': 3,
    'Vacuum': 5
}
base_wash = 10
total = base_wash

service_choice1 = input()
service_choice2 = input()

print("ZyCar Wash")
print("Base car wash - $10")

if service_choice1 != '-':
    cost1 = services[service_choice1]
    print(f"{service_choice1} - ${cost1}")
    total += cost1

if service_choice2 != '-':
    cost2 = services[service_choice2]
    print(f"{service_choice2} - ${cost2}")
    total += cost2


print("-----")
print(f"Total price: ${total}")

