# 1.12 zyLab training: Basics

user_num = int(input())
user_num_squared = user_num * user_num  # Bug here; fix it when instructed

print(user_num_squared)
# Output formatting issue here; fix it when instructed


# 1.13 zyLab training: Interleaved input / output

print('Enter x: ')
x = int(input())
 # Student mistakenly is echoing the input to output to match example
print('x doubled is:', (2 * x))

# 1.14 zyLab training*: One large program

print('Step 1 complete')
print('Step 2 as well')
print('All steps now complete')


# 1.18 LAB: Input: Mad Lib

# Read a value from a user and store the value in first_name
first_name = input()

# TODO: Type your code to read three more values here.\

whole_number = input()

plural_noun = input()

generic_location = input()
# Output a short story using the four input values. Do not modify the code below.
print(first_name, 'buys', whole_number, 'different types of', plural_noun, 'at', generic_location)

# 2.13 LAB: Divide input integers

user_num = int(input())
div_num = int(input())

num1 = user_num // div_num
num2 = num1 // div_num
num3 = num2 // div_num

print(num1, num2, num3)


# 2.14 LAB: Driving costs
gas_mileage = float(input())
cost_of_gas = float(input())

gas_cost_20 = (20 / gas_mileage) * cost_of_gas
gas_cost_75 = (75 / gas_mileage) * cost_of_gas
gas_cost_500 = (500 / gas_mileage) * cost_of_gas

print(f'{gas_cost_20:.2f} {gas_cost_75:.2f} {gas_cost_500:.2f}')


# 2.15 LAB: Expression for calories burned during workout

''' Calories = ((Age x 0.2757) + (Weight x 0.03295) + (Heart Rate x 1.0781) — 75.4991) x Time / 8.368 '''

Age = int(input())
Weight = int(input())
Heart_Rate = int(input())
Time = int(input())

Calories = ((Age * 0.2757) + (Weight * 0.03295) + (Heart_Rate * 1.0781) - 75.4991) * Time / 8.368
print(f'Calories: {Calories:.2f} calories')


# 2.16 LAB: Using math functions

import math

x = float(input())
y = float(input())
z = float(input())

power_x_z = x ** z
power_y_z = x ** (y ** z)
abs_x_y = abs(x - y)
sqrt_x_z = math.sqrt(x ** z)

print(f'{power_x_z:.2f} {power_y_z:.2f} {abs_x_y:.2f} {sqrt_x_z:.2f}')

# 2.17 LAB: Musical note frequencies

import math

f0 = float(input())

r = pow(2, 1/12)

f1 = f0 * pow(r, 1)
f2 = f0 * pow(r, 2)
f3 = f0 * pow(r, 3)

print(f'{f0:.2f} Hz')
print(f'{f1:.2f} Hz')
print(f'{f2:.2f} Hz')
print(f'{f3:.2f} Hz')

# 2.18 LAB: Convert to dollars

nickels = int(input())
dimes = int(input())
quarters = int(input())

total_amount = (nickels * 0.05) + (dimes * 0.10) + (quarters * 0.25)

print(f'Amount: ${total_amount:.2f}')

