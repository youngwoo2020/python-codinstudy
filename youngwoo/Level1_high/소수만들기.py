
nums = [1,2,7,6,4]

sum = 0

for i in range(len(nums)):
    print("***")
    print(nums[i])
    print("***")
    for j in range(len(nums)):
        if i!=j:
            for h in range(len(nums)):
                if j!=h:
                    print(nums[h])
            print("____")