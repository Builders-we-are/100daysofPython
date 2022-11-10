
nums = [{42}, (1, 2), (1, 2), [4, 5], 6, 7, 8, 8, 8, 8, 9, 10, 10, 10]

seen = dict()
res = []
for i in nums:
  if id(i) in seen:
    continue
  seen[id(i)] = True
  res.append(i)
print(res)

# [{42}, (1, 2), [4, 5], 6, 7, 8, 9, 10]