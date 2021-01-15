file = open('mat_dv.txt')
max_ball_alg = 0
maxsumball = 0
ball_geom, surnames, ball_alg, klass = [], [], [], []
for line in file:
    ball_geom.append(int(line.rpartition(' ')[-1]))
    ball_alg.append(int((line.rpartition(' ')[0]).rpartition(' ')[-1]))
    surnames.append(((line.rpartition(' ')[0]).rpartition(' ')[0]).rpartition(' ')[0])
    klass.append(((line.rpartition(' ')[0]).rpartition(' ')[0]).rpartition(' ')[-1])

for i in range(len(ball_alg)):

    d = {
        8: None,
        9: None,
        10: None,
        11: None
    }
    for key in d:
        if int(klass[i]) == key:
            summball = ball_geom[i] + ball_alg[i]
            if maxsumball < summball:
                maxsumball = summball

            d.update({key: str(maxsumball) + ' ' + str(surnames[i])})

    if ball_geom[i] == max(ball_geom):
        print(surnames[i], 'Набрал(а) максимальный балл по геометрии', max(ball_geom))
    if ball_alg[i] == max(ball_alg):
        print(surnames[i], ' Набрал максимальный балл по алгебре', max(ball_alg))
print(d)
