'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here

    # slice the array, find the largest in the window
    # increment the array right, arr[n] through arr[n+2], next becomes arr[n+1] through arr[n+3], etc
    # return the arr of max value from each respective window
    print(len(nums))
    catch = [0]*len(nums)
    count = 0
    


    for i in range(len(nums)-(k-1)):
        # while (count+(k-1)) <= len(nums):
        max_num = -100
        work = nums[i:(i+(k))]
        for j in work:
            if j >= max_num:
                max_num = j
                catch[i] = max_num
                count += 1
    final = [x for x in catch if x != 0]
    return final


    pass

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
