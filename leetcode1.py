def twoSum(nums, target):
    
    temp_dict = {}
    for num, item in enumerate(nums):
        if (target - item) in temp_dict:
            return sorted([num, temp_dict[target - item]])
        else:
            temp_dict[item] = num
    return False

print(twoSum([3,2,4],6))
