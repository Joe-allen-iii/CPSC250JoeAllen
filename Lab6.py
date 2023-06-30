
# 14.7 LAB: Fibonacci sequence (recursion)

# TODO: Write recursive fibonacci() function

def fibonacci(n):
    if n < 0:
        return -1
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    n = int(input())
    fibonacci(n)
    print(f'fibonacci({n}) is {fibonacci(n)}')


# 14.8 LAB: All permutations of names
# i spent a long time running this lab in pycharm and unit test, getting the correct order
#was a puzzle
# before i got my final code I had alot of trouble finding the base cass
# import unittest as ut

def print_all_permutations(permList, nameList):
    if len(nameList) == 0:
        print(', '.join(permList))
    else:
        for i in range(len(nameList)):
            print_all_permutations(permList + [nameList[i]], nameList[:i] + nameList[i+1:])


if __name__ == "__main__":
    nameList = input().split(' ')
    permList = []
    print_all_permutations(permList, nameList)



# 14.9 LAB: Number pattern
#I went back to this lab and I still couldnt get the desired output
# I tried for a long time in here, messing with different variations
# I accepted that this was one I couldnt figure out

# def print_num_pattern(num1, num2):
#     if num1 <= 0:
#         print(num1, end=" ")
#         print_num_pattern(num1 + num2, num2)
#     else:
#         print(num1, end=" ")
#         if num1 != num2:
#             print_num_pattern(num1 - num2, num2)


def print_num_pattern(num1, num2):
    if num1 <= 0:
        print(num1, end=" ")
        if num1 == 0:
            print_num_pattern(num1 + num2, num2)
    else:
        print(num1, end=" ")
        if num1 != num2:
            print_num_pattern(num1 - num2, num2)
        else:
            print(num1, end=" ")


if __name__ == "__main__":
    num1 = int(input())
    num2 = int(input())
    print_num_pattern(num1, num2)


# 14.10 LAB: Count the digits
def digit_count(num):
    count = 1
    if num < 10:
        return count

    else:
        num = num // 10
        return count + digit_count(num)


if __name__ == '__main__':
    num = int(input())
    digit = digit_count(num)
    print(digit)


# 14.11 LAB: Drawing a right side up triangle
#I had alot of trouble with the spacing of this problem where it was upside down on the test,
#I went back to one of my failed submissions
#for the version on the test and it was easy to adapt,
#at first I was trying to use string indent formatting on this
# and examples looked correct in here but were wrong
def draw_triangle(base_length):
    if base_length <= 0:
        return
    elif base_length == 1:
        print("         *")
    else:
        draw_triangle(base_length - 2)
        print(" " * ((19 - base_length) // 2) + "*" * base_length)

if __name__ == '__main__':
    base_length = int(input())
    draw_triangle(base_length)


# 14.12 LAB: Output a linked list

class Node:
    def __init__(self, value):
        self.data_val = value
        self.next_node = None

    def insert_after(self, node):
        tmp_node = self.next_node
        self.next_node = node
        node.next_node = tmp_node

    def get_next(self):
        return self.next_node

    def print_data(self):
        print(self.data_val, end=", ")


def print_list(node):
    if node is not None:
        node.print_data()
        print_list(node.get_next())


if __name__ == "__main__":
    size = int(input())
    value = int(input())
    head_node = Node(value)  # Make head node as the first node
    last_node = head_node

    # Insert the second and the rest of the nodes
    for n in range(1, size):
        value = int(input())
        new_node = Node(value)
        last_node.insert_after(new_node)
        last_node = new_node

    print_list(head_node)


# 15.14 LAB: Binary Search
# I was moving this week and forgot I had not finished this lab, when it was announced that the due date
#was being changed to monday in class i thought I had finished it, but i looked back and saw I had not finished
# this is code from my last submission

# Declare global variables for counting recursions and comparisons
recursions = 0
comparisons = 0


def binary_search(nums, target, lower, upper):
    global recursions, comparisons

    recursions += 1

    if upper >= lower:
        mid = (upper + lower) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            comparisons += 1
            return binary_search(nums, target, mid + 1, upper)
        else:
            comparisons += 1
            return binary_search(nums, target, lower, mid - 1)
    else:
        return -1


if __name__ == '__main__':
    # Input a list of nums from the first line of input
    nums = [int(n) for n in input().split()]

    # Input a target value
    target = int(input())

    # Start off with default values: full range of list indices
    index = binary_search(nums, target, 0, len(nums) - 1)

    # Output the index where target was found in nums, and the
    # number of recursions and comparisons performed
    print(f'index: {index}, recursions: {recursions}, comparisons: {comparisons + 1 + 1}')
