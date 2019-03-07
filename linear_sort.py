import random
numbers = [i for i in range(1, 11)]
random.shuffle(numbers)

def find_index_of_minimal_value(numbers):
    i = 1
    response = 0
    length = len(numbers) 
    if length == 1:
        return response
    value = numbers[0]
    while True:
        if (length-1) == i:
            return response 
        next_value = numbers[i]
        if next_value < value:
            value = next_value
            response = i
        i+=1

def linear_sort(numbers):
    length = len(numbers)
    i = 0

    while True:
        if (length-1) == i:
            return numbers 
        min_i = find_index_of_minimal_value(numbers[i:]) 
        numbers[i], numbers[i+min_i] = numbers[min_i+i], numbers[i]
        i+=1

print(linear_sort(numbers))
