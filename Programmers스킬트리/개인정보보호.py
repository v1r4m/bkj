def solution(today, terms, privacies):
    answer = []
    t = {}
    year,month,tday = today.split('.')
    tot = int(year)*12+int(month)
    for item in terms:
        key, month = item.split()
        t[key]=int(month)
    for i in range(len(privacies)):
        day, te = privacies[i].split()
        pmonth = int(t[te])
        syear,smonth,sday=day.split('.')
        stot = int(syear)*12+int(smonth)
        if tot-stot>pmonth:
            answer.append(i+1)
        elif tot-stot==pmonth:
            if int(tday)>=int(sday):
                answer.append(i+1)
    return answer
print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))