name = input()
numOfTeam = int(input())
teamList = []
probList = []
teamIndex = 0
maxPorb = 0;
for i in range(numOfTeam):
    teamList.append(input())
    L = name.count("L") + str(teamList[i]).count("L")
    O = name.count("O") + str(teamList[i]).count("O")
    V = name.count("V") + str(teamList[i]).count("V")
    E = name.count("E") + str(teamList[i]).count("E")
    num = ((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100
    probList.append((num, teamList[i]))
    
probList.sort(key=lambda x : (-x[0], x[1]))

print(probList[0][1])
