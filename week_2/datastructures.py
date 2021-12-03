# Tuple
# Data1 - Count the number of items
# Data1 - Find the value of the fourth item stored in the data set
# Data1 - Count the number of times 7 appears
Data1 = (7, False, "Apple", True, 7, 98.6) 
print(len(Data1))
print(Data1[3])
print(Data1.count(7))


# Set
# Data2 - Remove a random element from the data set
# Data2 - Add "Alpha" to the data set
# Data2 - Print data set
Data2 = {"July", 4, 8, "Tango", 4.3, "Bingo"}
Data2.pop()
Data2.add("Alpha")
print(Data2)


# List
# Data3 - Print the data set in reverse order
# Data3 - Change the second value in the data set to ‘B’
# Data3 - Remove the last item and print the data set
Data3 = ["A", 7, -1, 3.14, True, 7] 
Data3.reverse()
Data3[1] = "B"
Data3.pop(-1)
print(Data3)


# Dictionary
# Data4 - Change "active" to False
# Data4 - Add "address" with a value of "123 West Main Street"
# Data4 - Print the weekly salary for Joe if he worked a full 40 hour week.
# Data4 - Print the data set
Data4 =  {
 "name" : "Joe",
 "age" : 26,
 "active" : True, 
 "hourly_wage" : 14.75
}
Data4["active"] = False
Data4["address"] = "123 West Main Street"
pay_40_hours = Data4["hourly_wage"] * 40
print(pay_40_hours)
print(Data4)