# Project #2
# Test "Basic knowledge of programming".
# A user is offered several statements, the truth/falsity of which she/he must establish.
# The program displays the test result and evaluates it.


import local as lc

print(lc.TXT_TASK)

print(lc.TXT_STATEMENT, '1.\n', lc.TXT_STATEMENT1)
first = str.lower(input())

if first == 'true':
    points = 1
else:
    points = 0


print(lc.TXT_STATEMENT, '2.\n', lc.TXT_STATEMENT2)
second = str.lower(input())

if second == 'true':
    points = points + 1


print(lc.TXT_STATEMENT, '3.\n', lc.TXT_STATEMENT3)
third = str.lower(input())

if third == 'true':
    points = points + 1


print(lc.TXT_STATEMENT, '4.\n', lc.TXT_STATEMENT4)
fourth = str.lower(input())

if fourth == 'true':
    points = points + 1


print(lc.TXT_STATEMENT, '5.\n', lc.TXT_STATEMENT5)
fifth = str.lower(input())

if fifth == 'false':
    points = points + 1


print(lc.TXT_STATEMENT, '6.\n', lc.TXT_STATEMENT6)
sixth = str.lower(input())

if sixth == 'true':
    points = points + 1


print(lc.TXT_STATEMENT, '7.\n', lc.TXT_STATEMENT7)
seventh = str.lower(input())

if seventh == 'true':
    points = points + 1


print(lc.TXT_STATEMENT, '8.\n', lc.TXT_STATEMENT8)
eighth = str.lower(input())

if eighth == 'true':
    points = points + 1


print(lc.TXT_STATEMENT, '9.\n', lc.TXT_STATEMENT9)
ninth = str.lower(input())

if ninth == 'false':
    points = points + 1


print(lc.TXT_STATEMENT, '10.\n', lc.TXT_STATEMENT10)
tenth = str.lower(input())

if tenth == 'false':
    points = points + 1


print(lc.TXT_STATEMENT, '11.\n', lc.TXT_STATEMENT11)
eleventh = str.lower(input())

if eleventh == 'false':
    points = points + 1


print(lc.TXT_STATEMENT, '12.\n', lc.TXT_STATEMENT12)
twelfth = str.lower(input())

if twelfth == 'true':
    points = points + 1


result = round(points / 12 * 100)
print(lc.TXT_CONCLUSION, result, '%.')

if result >= 70:
    print(lc.TXT_GREATRESULT)
elif result >= 50:
    print(lc.TXT_GOODRESULT)
else:
    print(lc.TXT_BADRESULT)
