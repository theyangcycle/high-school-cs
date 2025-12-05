a = int(input())
for b in range(a):
    agent = []
    score = []
    teams = []
    inp = input().split(' ')
    for i in range(len(inp)):
        x = inp[i].split('=')
        agent.append(x[0])
        score.append(x[1])
    
    score = list(map(int,score))
    paired = list(zip(score,agent))
    paired.sort()
    score,agent = zip(*paired)
    score,agent = list(score),list(agent)
    
    for i in range(len(agent)):
        team = []
        team.append(agent[i])
        for j in range(len(agent)):
            if 0 <= score[j] - score[i] <= 10:
                if agent[j] not in team:
                    team.append(agent[j])
        
        teams.append(team)
    
    teams = list(map(sorted,teams))
    teams.sort()
    print(' '.join(max(teams,key=len)))