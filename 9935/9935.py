a = input()
b = input()

# import time, random, string

# letters_set = string.ascii_lowercase
# a = ''.join([random.choice(letters_set) for i in range(10000)])
# b = ''.join([random.choice(letters_set) for i in range(36)])

# starttime = time.time()
# a = "mirkovC4nizCC44"
# b = "C4"

queue = []
def checkmoon(list, b):
    for i in range(len(list)):
        if list[i]==b[i]:
            continue
        else:
            return False
    return True

for i in range(len(a)):
    queue.append(a[i])
    if len(queue)>=len(b):
        if checkmoon(queue[-1*len(b):],b):
            for j in range(len(b)):
                queue.pop()


resultstring = ''.join(queue)
if resultstring == '':
    resultstring = "FRULA"
print(resultstring)
# endtime = time.time()
# print(endtime-starttime)