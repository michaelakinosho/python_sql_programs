# Credit: source of solution is AlgoExpert provided solution
def largestRange(array):
    bestRange = []
    longestLength = 0
    nums = {}
    for num in array:
        nums[num] = True
    for num in array:
        print(nums)
        if not nums[num]:
            #print(f"This number {num} is already False")
            continue
        nums[num] = False
        #print(f"This is number {num}")
        currentLength = 1
        left = num - 1
        right = num + 1
        while left in nums:
            nums[left] = False
            currentLength += 1
            left -= 1
        while right in nums:
            nums[right] = False
            currentLength += 1
            right += 1
        if currentLength > longestLength:
            longestLength = currentLength
            bestRange = [left + 1, right - 1]
    return bestRange


largestRange([1,11,3,0,15,5,2,4,10,7,12,6])