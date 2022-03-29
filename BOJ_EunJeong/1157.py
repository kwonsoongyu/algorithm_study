s = input().upper()     # 대소문자 구분이 없으므로 upper()로 대문자로 통일
s_list = list(set(s))   # set()으로 받은 문자열의 중복을 없앤 뒤 list로 만듬

num_list = []           # 존재하는 알파벳의 개수가 들어갈 배열
for i in s_list:        # 중복제거된 문자열의 개수만큼 반복
    num_list.append(s.count(i))

if num_list.count(max(num_list))>1:
    print("?")
else:
    print(s_list[(num_list.index(max(num_list)))])
