def makeArr(arr, ord):
  n = len(arr)
  if n < 3:
    return
  else:
    arr_list = []
    for i in arr:
      arr_list.append(i[ord * n : (ord+1) *n ])
    return arr_list

def checkArr(group):
  first = group[0][0]
  for i in group:
    for j in i:
      if j == first:
        continue
      else:
        return 2
  return first

def addNum(check_num, gbb):
  if check_num == -1:
    gbb[0] += 1
    return gbb
  elif check_num == 0:
    gbb[1] += 1
    return gbb
  else:
    gbb[2] += 1
    return gbb

def splitNum(numbers, n, gbb):
  if n <= 1:
    if numbers[0] == -1:
      gbb[0] += 1
      return gbb
    elif numbers[0] == 0:
      gbb[1] += 1
      return gbb
    else:
      gbb[2] += 1
      return gbb
  spl = n // 3
  group1 = makeArr(numbers[0:spl],0)
  group2 = makeArr(numbers[0:spl],1)
  group3 = makeArr(numbers[0:spl],2)
  group4 = makeArr(numbers[spl:2*spl],0)
  group5 = makeArr(numbers[spl:2*spl],1)
  group6 = makeArr(numbers[spl:2*spl],2)
  group7 = makeArr(numbers[2*spl:],0)
  group8 = makeArr(numbers[2*spl:],1)
  group9 = makeArr(numbers[2*spl:],2)

  check_num1 = checkArr(group1)
  if check_num1 == 2:
    splitNum(group1,len(group1), gbb)
  else:
    gbb = addNum(check_num1, gbb)

  check_num2 = checkArr(group2)
  if check_num2 == 2:
    splitNum(group2,len(group2), gbb)
  else:
    gbb = addNum(check_num2, gbb)
  
  check_num3 = checkArr(group3)
  if check_num3 == 2:
    splitNum(group3,len(group3), gbb)
  else:
    gbb = addNum(check_num3, gbb)
  
  check_num4 = checkArr(group4)
  if check_num4 == 2:
    splitNum(group4,len(group4), gbb)
  else:
    gbb = addNum(check_num4, gbb)
  check_num5 = checkArr(group5)
  if check_num5 == 2:
    splitNum(group5, len(group5),gbb)
  else:
    gbb = addNum(check_num5, gbb)
  
  check_num6 = checkArr(group6)
  if check_num6 == 2:
    splitNum(group6, len(group6),gbb)
  else:
    gbb = addNum(check_num6, gbb)
  
  check_num7 = checkArr(group7)
  if check_num7 == 2:
    splitNum(group7, len(group7),gbb)
  else:
    gbb = addNum(check_num7, gbb)
  check_num8 = checkArr(group8)
  if check_num8 == 2:
    splitNum(group8, len(group8),gbb)
  else:
    gbb = addNum(check_num8, gbb)
  
  check_num9 = checkArr(group9)
  if check_num9 == 2:
    splitNum(group9,len(group9), gbb)
  else:
    gbb = addNum(check_num9, gbb)
  return gbb
    
def mergeSort(numbers, gbb):
    n = len(numbers)
    gbb = splitNum(numbers, n ,gbb)
      
    return gbb

numbers = []
n = int(input())
gbb = [0, 0, 0]
for _ in range(n):
    numbers.append(list(map(int,input().split())))

gbb_list = mergeSort(numbers, gbb)

for i in gbb_list:
  print(i)

