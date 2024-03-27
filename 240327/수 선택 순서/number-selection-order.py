from collections import deque

n, x = map(int, input().split())
numbers = list(map(int, input().split()))
queue = deque([(num, idx) for idx, num in enumerate(numbers)])

cnt = 0
while queue:
    # 현재 큐의 최댓값을 계산합니다.
    current_max = max(num for num, idx in queue)
    
    num, idx = queue.popleft()
    if num == current_max:
        # 현재 숫자가 최댓값일 경우, 카운트를 증가시키고,
        # 해당 숫자가 목표 인덱스일 경우, 반복을 종료합니다.
        cnt += 1
        if idx == x:
            break
    else:
        # 현재 숫자가 최댓값이 아닐 경우, 큐의 끝으로 보냅니다.
        queue.append((num, idx))

print(cnt)