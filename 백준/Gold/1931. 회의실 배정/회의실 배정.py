n = int(input())
meetings = []

for _ in range(n):
    start, end = map(int,input().split())
    meetings.append((start, end))
    
meetings.sort(key=lambda x:(x[1], x[0]))

count = 0
현재끝난시간 = 0

for start, end in meetings:
    if start >= 현재끝난시간:
        count += 1
        현재끝난시간 = end

print(count)
        