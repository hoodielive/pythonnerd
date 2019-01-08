# one-dimensional
one_dimensional_array = [1,2,3,4,5]

print(one_dimensional_array[0]) # O(1) -> if you specify index

# two-dimensional 
two_dimensional_array = [1, 2, 300, 3, 4, 5]

# for loop O(n)
for num in two_dimensional_array:
    print(num); 

# insert O(n)
two_dimensional_array[1] = "Insert"

# for loop O(n)
for i in range(len(two_dimensional_array)):
    print(two_dimensional_array[i])

# print first 2 indices O(1)
print(two_dimensional_array[0:2])

# Linear search maximum O(n)
maximum = numbers[0]

for num in two_dimensional_array:
    if num > maximum:
        maximum = num

print(maximum)
