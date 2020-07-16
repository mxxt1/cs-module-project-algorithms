'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    # loop through array and count instances of the element, if the element only shows up once it's the single element
    # loop through the array using a hash table to cache repeating numbers, if number exists in table increment count +1, don't add new entry, move to next number. if number doesn't exist in table, move forward. If we hit the end, the number with 1 instance is the number
    
    # I could have done this with a list lol
    cache = {}
    
    for number in arr:
        if number in cache:
            del cache[number]
        else:
            cache[number] = 1
    return list(cache.keys())[0]
    



    pass


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")