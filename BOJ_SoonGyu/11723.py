import sys
#11723
input = sys.stdin.readline

M = int(input())
data = set()

for i in range(M):
    word = input().strip().split()

    if len(word) == 1:
        if word[0] =="all":
            data = set(i for i in range(1,21))
        else:
            data = set()

    else:
        command, num = word[0],word[1]
        num = int(num)

        if command == "add":
            data.add(num)
        elif command == "remove":
            data.discard(num)
        elif command == "check":
            if num in data:
                print("1")
            else:
                print("0")
        elif command == "toggle":
            if num in data:
                data.discard(num)
            else:
                data.add(num)




