n = int(input())
digits = list(map(int, input().split()))

cnt0 = digits.count(0)
cnt5 = digits.count(5)

# No zero → cannot be divisible by 10
if cnt0 == 0:
    print(-1)
    exit()

# Not enough 5s to make sum divisible by 9
if cnt5 < 9:
    print(0)
    exit()

# Use maximum multiple of 9 fives
use5 = (cnt5 // 9) * 9

# Construct result
result = "5" * use5 + "0" * cnt0
print(result)
