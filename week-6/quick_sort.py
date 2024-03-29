import time
import random


def quick_sort(a_list, start, end):
    # list size is 1 or less (which doesn't make sense)
    if start >= end:
        return

    # Call the partition helper function to split the list into two section 
    # divided between a pivot point
    pivot = partitionAtRandom(a_list, start, end)
    quick_sort(a_list, start, pivot-1)
    quick_sort(a_list, pivot+1, end)
        

def partitionStart(a_list, start, end):
    #selects the first value on the list (index 0)
    return partition(a_list, start, end)
# First Run Time: 0.002032041549682617
# Second Run Time: 0.001001119613647461
# Third Run Time: 0.0009996891021728516  Fastest



# ---------------------------------------------------------------------  Start of changes...
# Swapped the start and ending values
def partitionEnd(a_list, start, end):
    a_list[start], a_list[end -1] = a_list[end-1], a_list[start]
    return partition(a_list, start, end)
# First Run Time: 0.0019989013671875
# Second Run Time: 0.002001523971557617
# Third Run Time: 0.0010013580322265625  Fastest

# Using the middle value as pivot
def partitionMiddle(a_list, start, end):
    mid_point = int(len(a_list)) //2
    a_list[start], a_list[mid_point] = a_list[mid_point], a_list[start]
    return partition(a_list, start, end)
# First Run Time: 0.0019991397857666016
# Second Run Time: 0.0019979476928710938  Fastest
# Third Run Time: 0.0020020008087158203

# Selecting a random index in the list as a pivot
def partitionAtRandom(a_list, start, end):
    ran_index = random.randint(0,len(a_list)-1)
    a_list[start], a_list[ran_index] = a_list[ran_index], a_list[start]
    return partition(a_list, start, end)
# First Run Time: 0.002991199493408203  Fastest
# Second Run Time: 0.0030002593994140625
# Third Run Time: 0.0029985904693603516


# Fastest times from each different pivot selection after 3 runs each:
# start    0.0009996891021728516
# end      0.0010013580322265625
# middle   0.0019979476928710938
# random   0.002991199493408203

# Fastest Overall is the pivot selection at the start.

# ---------------------------------------------------------------- End of changes



def partition(a_list, start, end):
    # Select the first element as our pivot point
    pivot = a_list[start]
    
    # Start at the first element past the pivot point
    low = start + 1
    high = end

    while True:
        # If the current value we're looking at is larger than the pivot
        # it's in the right place (right side of pivot) and we can move left,
        # to the next element.
        # We also need to make sure we haven't surpassed the low pointer, since that
        # indicates we have already moved all the elements to their correct side of the pivot
        while low <= high and a_list[high] >= pivot:
            high = high - 1

        # Opposite process of the one above
        while low <= high and a_list[low] <= pivot:
            low = low + 1

        # We either found a value for both high and low that is out of order
        # or low is higher than high, in which case we exit the loop
        if low <= high:
            # Swap the values
            a_list[low], a_list[high] = a_list[high], a_list[low]
            # The loop continues
        else:
            # We exit out of the loop
            break

    # Swap the values
    a_list[start], a_list[high] = a_list[high], a_list[start]

    return high


print("Quick Sort:")
myList = [54,26,93,17,77,31]
myList = [x for x in range(1000)]
random.shuffle(myList)

# print(myList)
start_time = time.time()
quick_sort(myList,0,len(myList)-1)
end_time = time.time()
# print()
# print("Sorted Listed: ")
# print(myList)   

print(f"The execution time is: {end_time-start_time}")



