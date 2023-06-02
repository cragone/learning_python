input = [2, 7, 9, 5, 1, 3, 5]

def max_range(arr):
#sorting original array setting a new list
    #arr.sort()
    arr2 = []
#finding the differences and putting them in a list
    digit = arr[0]
    for num in range(len(arr) - 1):
        diff = abs(arr[num+1] - arr[num])
        arr2.append(diff)
    #print(arr2)
#after appending, we attempt to find the max
    var = 0
    for num2 in arr2:
        if num2 > var:
            var = num2

    return var
    
print(max_range(input))