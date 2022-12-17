# 구현문제 예제 4-2 시각

# 내가 푼 풀이

n = int(input())
count = 0

time = []

# 초, 분, 시는 i,j,k로 하자
for k in range(n + 1):
  for j in range(60):
    for i in range(60):
      if i % 10 == 3 or i // 10 == 3 or j % 10 == 3 or j // 10 == 3 or k % 10 == 3 or k // 10 == 3:
        count += 1

print(count)

#3이 포함되는 수는 3,13,23,43,53
# 30~39

#놓친 포인트
# 03분 00초~59초는 count+=1이 아니라 += 60이다

# 첫째 시도
# '분'부분에서 count += 60으로 수정
# '시'부분에서 count += 60*60으로 수정
# fail..수가 중복으로 더해짐
# 그러면 if문을 한번만 쓰면 되잖아??
# 드디어 해결
