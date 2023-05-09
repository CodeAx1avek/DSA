def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1,(len(nums))):
            if i !=j and nums[i] + nums[j] == target:
                return [i,j]
    return []

a = twoSum([1,2,6],8)
print(a)