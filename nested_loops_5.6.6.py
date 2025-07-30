lst = list(map(int, input().split()))

for i in range(len(lst)):
	j = lst.index(min(lst[i:]), i, len(lst))
	lst[i], lst[j] = lst[j], lst[i]
print(*lst)