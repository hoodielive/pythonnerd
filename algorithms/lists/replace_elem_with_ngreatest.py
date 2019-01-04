# Replace each element in a list with the next greatest

A = [0, 2, 8, 1, 3, 5, 4]

# a non-empty list in which each element should be replaced with the next greatest 
def replace_with_next_greatest(a):
    n = len(a)

    next_greatest = a[n-1]
    a[n-1] = "INVALID_NUMBER"

    # Process the list from the back 
    for i in range(n-2, -1, -1):
        temp = a[i]

        a[i] = next_greatest

        if (temp > next_greatest):
            next_greatest = temp
            print(next_greatest) 

replace_with_next_greatest(A)
