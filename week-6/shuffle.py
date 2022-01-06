import random

my_list = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]


def shuffle_algorithm(my_list):
        # Fisher Yates Algorithm time complexity = O(n)
    for i in range(len(my_list)-1, 0, -1):
        # Generating a random index from 0 to i + 1
        r = random.randint(0, i + 1)
        # Swap i with the element at random index
        my_list[i], my_list[r] = my_list[r], my_list[i]
    return my_list


print(my_list)
print(shuffle_algorithm(my_list))
print(shuffle_algorithm(my_list))
print(shuffle_algorithm(my_list))
print(shuffle_algorithm(my_list))



