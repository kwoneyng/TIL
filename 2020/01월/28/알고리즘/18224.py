from collections import deque

def answer(t):
	if t % (m*2) >= m:
		rs = str(t // (m*2) + 1) + ' moon'
	else:
		rs = str(t // (m*2) + 1) + ' sun'
	print(rs)

near = [[-1,0],[0,1],[1,0],[0,-1]]
n,m = map(int,input().split())
bd = [list(map(int,input().split())) for i in range(n)]

q = deque([(0,0)])
t = 0
stop = 0
vis = [[5000]*n for i in range(n)]
while q and stop == 0:
	time = (t+m)//(2*m)
	for i in range(len(q)):
		if stop:
			break
		x,y = q.popleft()
		for a,b in near:
			xi, yi = x+a, y+b
			# 벽 안넘고 종료
			if xi == n-1 and yi == n-1:
				answer(t)
				stop = 1
				break
			if t % (2*m) < m: # 낮
				if 0 <= xi < n and 0 <= yi < n and (vis[xi][yi]+m)//(2*m) >= time and bd[xi][yi] == 0:
					if vis[xi][yi] != t:
						q.append((xi,yi))
					vis[xi][yi] = t

			elif t % (2*m) >= m: # 밤
				if 0 <=xi < n and 0 <= yi < n:
					if bd[xi][yi] == 1: # 벽 넘기
						while 0 <= xi < n and 0 <= yi < n and bd[xi][yi] == 1:
							xi += a
							yi += b
						if 0 <= xi < n and 0 <= yi < n:
							if xi == n-1 and yi == n-1:
								answer(t)
								stop = 1
								break
							if (vis[xi][yi]+m)//(2*m) >= time:
								if vis[xi][yi] != t:
									q.append((xi,yi))
								vis[xi][yi] = t
					elif (vis[xi][yi]+m)//(2*m) >= time:
						if vis[xi][yi] != t:
							q.append((xi,yi))
						vis[xi][yi] = t
	t += 1		
if stop == 0:
	print(-1)

# 10 3
# 0 1 1 1 1 1 1 1 1 1
# 0 1 1 1 1 1 1 1 1 1
# 0 1 1 1 1 1 1 1 1 1
# 0 1 1 1 1 1 1 1 1 1
# 0 1 1 1 1 1 1 1 1 1
# 0 1 0 0 1 1 1 1 1 0
# 1 1 1 1 1 1 1 1 1 0
# 1 1 1 1 1 1 1 1 1 0
# 1 1 1 1 1 1 1 1 1 0
# 1 1 0 1 1 1 1 1 1 0