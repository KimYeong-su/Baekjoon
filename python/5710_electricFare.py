import sys
input = sys.stdin.readline
# 가격 요금 : 200, 29700, 4950000
while True:
    A,B = map(int, input().split())
    if A == B == 0:
        exit()
    
    # 두사람이 사용한 전기량
    if A <= 200:
        use = A//2 
    elif 200 < A <= 29700:
        use = (A-200) // 3 + 100
    elif 29700 < A <= 4950000:
        use = (A-29900) // 5 + 100 + 9900
    else:
        use = (A-200-29700-4950000) // 7 + 100 + 9900 + 990000

    def charge(watt):
        if watt <= 100:
            return watt * 2
        elif 100 < watt <= 10000:
            return 200 + (watt-100) * 3
        elif 10000<= watt < 1000000:
            return 200 + 29700 + (watt-10000) * 5
        else:
            return 200 + 29700 + 4950000 + (watt-1000000) * 7
    
    left = 0
    right = use

    while left <= right:
        mid = (left + right) // 2

        charge_a = charge(mid)
        charge_b = charge(use-mid)

        if abs(charge_b - charge_a) > B:
            left = mid + 1
        else:
            if abs(charge_b - charge_a) == B:
                print(min(charge_a,charge_b))
                break
            right = mid - 1