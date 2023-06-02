def factorial_number(num):
    if num == 0 or num == 1:
        return 1
    else:
        return factorial_number(num-1) *num
print(factorial_number(3))