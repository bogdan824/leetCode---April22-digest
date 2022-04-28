def concat (nums,target):
	count = 0
	for i in range(len(nums)):
		for j in range(len(nums)):
			if nums[i]+nums[j]==target:
				count+=1
	print(count) 


nums = ["777","7","77","77"]
target = "7777"

concat(nums,target)