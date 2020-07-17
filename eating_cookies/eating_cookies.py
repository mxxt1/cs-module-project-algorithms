'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    
    if n <= 3:
        if n == 3:
            return 4
        elif n ==2: 
            return 2
        elif n == 1:
            return 1
        elif n == 0:
            return 1
        else:
            return 0
    else:
        back_3 = 1
        back_2 = 2
        back_1 = 4
        current = back_1+back_2+back_3
        counter = 4

        while counter < n:
            back_3 = back_2
            back_2 = back_1
            back_1 = current
            current = back_1+back_2+back_3
            counter += 1
    return current

    pass

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
