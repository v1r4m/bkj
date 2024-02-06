def solution(friends, gifts):
    fdict = {}
    gdict = {}
    final = {}
    real = {}
    for i in range(len(friends)):
        fdict[friends[i]]=0
        final[friends[i]]=0
        real[friends[i]]=0
    for i in range(len(gifts)):
        cursor = gifts[i]
        giver, receiver = cursor.split()
        final[giver] += -1
        final[receiver] += 1
        if cursor in gdict:
            gdict[cursor] += 1
        else:
            if receiver+' '+giver in gdict:
                gdict[receiver+' '+giver] += -1
            else:
                gdict[cursor] = 1
        fdict[giver] += 1
        fdict[receiver] += -1
    #end of loop
    for i in friends:
        for j in friends:
            if i!=j:
                if i+' '+j in gdict:
                    pass
                elif j+' '+i in gdict:
                    pass
                else:
                    gdict[i+' '+j] =0
    for cursor,value in gdict.items():
        giver,receiver = cursor.split()
        if value<0:
            gdict[cursor] += 1
            final[giver]+= -1
            final[receiver] += 1
            real[receiver]+= 1
        elif value == 0: #두번째조건
            if fdict[giver]==fdict[receiver]:
                pass # 아무것도 하지않음
            elif fdict[giver]>fdict[receiver]: #r->g
                gdict[cursor] += -1
                final[giver] += 1
                final[receiver] += -1
                real[giver]+=1
                
            else: #g->r
                gdict[cursor] += 1
                final[receiver] += 1
                final[giver] += -1
                real[receiver]+=1
        else:
            gdict[cursor] += -1
            final[giver]+=1
            final[receiver] += -1
            real[giver]+=1
    answer = 0
    for key,value in real.items():
        if value>answer:
            answer = value
        
    return answer

print(solution(["muzi", "ryan", "frodo", "neo"], ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]))