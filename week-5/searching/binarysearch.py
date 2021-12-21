lst1 = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]   # find 31
lst2 = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]   # find 77
lst3 = ["Alpha", "Beta", "Delta", "Epsilon", "Gamma", "Theta", "Zeta"]   # find "Delta"


def binarySearch(sorted_list, term):
    length_of_list = len(sorted_list)
    first_element = 0
    last_element = (length_of_list) -1
    while first_element <= last_element:
        mid_point = (last_element + last_element) // 2
        if sorted_list[mid_point] == term:
            return True
        if term > sorted_list[mid_point]:
            first_element = mid_point + 1
        else:
            last_element = mid_point - 1
            
    if first_element > last_element:
        return False
    
    
print(binarySearch(lst1, 31))
print(binarySearch(lst2, 77))
print(binarySearch(lst3, "Delta"))
            