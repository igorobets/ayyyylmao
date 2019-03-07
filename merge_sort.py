import random
numbers = [i for i in range(1, 101)]
random.shuffle(numbers)

def _merge(left_array, right_array):
    result = [ 0 for _ in range(len(left_array)+len(right_array))]
    res_i = left_i = right_i = 0

    while True:
        cur_left = cur_right = None

        if left_i < len(left_array):
            cur_left = left_array[left_i]

        if right_i < len(right_array):
            cur_right = right_array[right_i]

        if cur_left and cur_right: 
            if cur_left <= cur_right:
                result[res_i] = cur_left  
                left_i+=1
            elif cur_left > cur_right:
                result[res_i] = cur_right
                right_i+=1
        elif cur_left:
            result[res_i] = cur_left  
            left_i+=1
        elif cur_right:
            result[res_i] = cur_right
            right_i+=1
        else:
            print('error')
        res_i+=1
        if res_i == len(result):
            return result

def merge_sort(numbers):
    if len(numbers) < 2:
        return numbers
    return _merge(merge_sort(numbers[:len(numbers)//2]), merge_sort(numbers[len(numbers)//2:]))

print(merge_sort(numbers))
