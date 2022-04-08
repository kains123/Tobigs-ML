def merge_sort(numbers):

    n = len(numbers)

    if n <= 1:
        return

    mid = n // 2
    left_group = numbers[:mid]
    right_group = numbers[mid:]
    
    merge_sort(left_group)
    merge_sort(right_group)

    left = 0
    right = 0
    now = 0

    while left < len(left_group) and right < len(right_group):
        if left_group[left] < right_group[right]:
            numbers[now] = left_group[left]
            left += 1
            now += 1
        else:
            numbers[now] = right_group[right]
            right += 1
            now += 1

    while left < len(left_group):
        numbers[now] = left_group[left]
        left += 1
        now += 1

    while right < len(right_group):
        numbers[now] = right_group[right]
        right += 1
        now += 1
    
    return numbers

numbers =list(map(int, input().split()))

arranged_numbers = merge_sort(numbers)


for i in range(len(arranged_numbers)):
	print(arranged_numbers[i])

