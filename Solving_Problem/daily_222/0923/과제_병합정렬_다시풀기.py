def merge_sort(m):
   if len(m) <= 1:
       return m
   mid = len(m)//2
   left = m[:mid]
   right = m[mid:]
   left = merge_sort(left)
   right = merge_sort(right)
   return merge(left, right)
# 병합
def merge(left, right):
   global cnt
   result = []
   if left[-1] > right[-1]:
       cnt += 1
   l = h = 0
   while len(left) > l and len(right) > h:
       if left[l] <= right[h]:
           result.append(left[l])
           l+=1
       else:
           result.append(right[h])
           h += 1
   if len(left) > 0:
       result += left[l:]
   if len(right) > 0:
       result += right[h:]
   return result
for tc in range(int(input())):
   idx = int(input())
   arr = list(map(int, input().split()))
   cnt = 0
   arr = merge_sort(arr)
   print(f'#{tc+1} {arr[idx//2]} {cnt}')