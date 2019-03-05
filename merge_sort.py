import random
numbers = random.shufle([i for i in range(1, 101)])
def _merge(left_array, right_array):
    result = [ 0 for _ in range(len(left_array)+len(right_array))]
    res_i, left_i, right_i = 0
    while True:
        cur_left = left_array[left_i]
        cur_right = right_array[right_array]
        if cur_left <= cur_right:
            result[res_i] = cur_left  
        elif cur_left > cur_right:
            result[res_i] = cur_right
        else:
            print('error')



def merge_sort(numbers):
