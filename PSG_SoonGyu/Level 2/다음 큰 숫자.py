def solution(n):
    answer = 0
    num = n
    res = []
    sum1 = 0
    sum2 = 0
    while True:
        res.append(num % 2)
        num = num // 2
        if num == 0:
            break
    for i in range(len(res)):
        if res[i] == 1:
            sum1 += 1

    result = []
    for i in range(n + 1, n * 2):
        k = i
        sum2 = 0
        for j in range(len(res)+1):
            result.append(k % 2)
            k = k // 2
        for t in result:
            if t == 1:
                sum2 += 1
        if sum1 == sum2:
            answer = i
            break

        result.clear()

    print(answer)

    return answer
