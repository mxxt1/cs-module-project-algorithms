'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here

    # count the number of zeros, push non-zeros to a catch array
    # append the number of zeros from the count
    # return the array

    numbers = []
    count = 0

    for number in arr:
        if type(number) is int and number == 0:
            count += 1
        elif type(number) is int:
            numbers.append(number)
    
    while count > 0:
        numbers.append(0)
        count -= 1
    

    return numbers



if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")