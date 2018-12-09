# add/remove operations:: linear time vs constant time complexity 
# O(1) constant time is fast because you know the index, therefore you don't have to revert to searching
# O(N) linear search is slow because you do not know the index and it has to be sought

array = [34, 12, 120, -5]
print(array)

# quickly remove the last index - fast because you have specified the index; O(1)
def removeLast():
    array.pop() 
    print(array)

removeLast()

# arrays in python are called lists
numbers = [10, 20, 30, 40, 50] # one dimensional array/list 

# random indexing -> O(1) get items if we know the index
print(numbers[0])

numbers[1] = 200
print(numbers[1])

for number in numbers:
    print(number)

# O(N) linear search run time complexity - not fast because you don't know the index
maximum = numbers[0]
for num in numbers:
    if num > maximum:
        maximum = num

# print the result of linear search 
print(maximum)
