example = [3,16,27,7,3,25,9,30,7,9]

def find_maximum_minimum(nums):
    if len(nums) == 0:
        print("Empty list")
        return 
    
    maximum = minimum = nums[0]

    for num in nums:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num

    print("maximum:", maximum)
    print("minimum:", minimum)

find_maximum_minimum(example)