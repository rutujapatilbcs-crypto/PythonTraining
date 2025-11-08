nums=[78,19,13,9,18]

for num in nums:
    if num % 5==0:
        print(num)
        break
else:
    print("Not found")