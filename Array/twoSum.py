def brute_force(nums, target):

    for i in range(0, len(nums)):
        for j in range(0, len(nums)):
            if i != j and nums[i] + nums[j] == target:
                return [i, j]

my_list = [2,7,11,15]
my_target = 9

print(brute_force(my_list, my_target))
