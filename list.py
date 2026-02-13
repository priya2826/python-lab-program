
nums = [10, 20, 30, 40, 50]
print("Original:", nums)

nums.append(60)
nums.insert(1, 15)
nums.remove(30)

nums.pop()
print("Modified:", nums)

nums.sort()
print("Sorted:", nums)

nums.reverse()
print("Reversed:", nums)

print("Length:", len(nums))
print("Max:", max(nums))
print("Min:", min(nums))
print("Sum:", sum(nums))

new_list = nums.copy()
print("Copied List:", new_list)

nums.clear()
print("Cleared List:", nums)
