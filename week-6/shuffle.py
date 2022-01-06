import random

my_list = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]
print("Before Shuffle: ", my_list)


# Algorithm time complexity = O(n)
for i in range(len(my_list)-1, 0, -1):
    
    # Generating a random index from 0 to i + 1
    j = random.randint(0, i + 1)

    # Swap i with the element at random index
    my_list[i], my_list[j] = my_list[j], my_list[i]

print("After shuffle: ", my_list)


