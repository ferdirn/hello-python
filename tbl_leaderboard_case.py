#!/usr/bin/env python

leaderboard = [(7, 30), (3, 20), (4, 20), (5, 20), (6, 20), (1, 10), (2, 10)]

print "leaderboard: ", leaderboard
print
print "id sorting"

tmp = []
resp = []
last_score = None

for l in leaderboard:
    score = l[1]
    if score != last_score:
        if len(tmp):
            tmp.reverse()
            resp = resp + tmp
            tmp = []
            tmp.append(l)
        else:
            tmp.append(l)
    else:
        tmp.append(l)
    last_score = score

tmp.reverse()
resp = resp + tmp

print
print "result: ", resp
