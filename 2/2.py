N, M, Q, cw, sw, hw, tw = map(int, input().split())
sum = 0
fl = True
allRait = 0
maximum = 0
average = 0
minimum = 0
nameThree = ''
nameOne = ''
nameTwo = ''
one = 0
two = 0
three = 0
if M <= 0 or cw <= 0 or sw <= 0 or hw <= 0 or tw <= 0 or N < 3:
    fl = False
else:
    for _ in range(N):
        name = input()
        sum = 0
        for _ in range(M):
            a, b, c, d = map(int, input().split(","))
            if a >= 0 and b >= 0 and c >= 0 and d >= 0:
                sum += a * cw + b * sw + c * hw + d * tw
            else: 
                fl = False
        if sum <= Q:
            allRait += sum
            if maximum == 0:
                maximum = sum
                one = sum
                nameOne = name
            elif sum > maximum:
                three = two
                nameThree = nameTwo
                two = maximum
                nameTwo = nameOne
                maximum = sum
                one = sum
                nameOne = name
            elif sum > two:
                three = two
                nameThree = nameTwo
                two = sum
                nameTwo = name
            elif sum > three:
                three = sum
                nameThree = name
            if minimum == 0:
                minimum = sum
            elif sum < minimum:
                minimum = sum
        else:
            fl = False
if fl:
    average = round((allRait / N / Q) * 100)
    maximum = round((maximum / Q) * 100)
    minimum = round((minimum / Q) * 100)
    one = round((one / Q) * 100)
    two = round((two / Q) * 100)
    three = round((three / Q) * 100)
    print(maximum, average, minimum)
    print(f'{nameOne} {one}%')
    print(f'{nameTwo} {two}%')
    print(f'{nameThree} {three}%')
    if average <= 50: 
        print('Курс усваивается плохо')
    else: 
        print('Курс усваивается хорошо')
else:
    print("Во введённых данных ошибка")