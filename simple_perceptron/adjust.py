def change(weight_k, X_k, LR, sign):
    return weight_k + LR * X_k * (sign)

def weight_adjust(Xin, hot_one, expected, weights, LR=0.01):
    for i in range(len(hot_one)):
        if hot_one[i] == expected[i]:
            # then the answer classification is correct
            pass
        else:
            weights[i][0] = weights[i][0] + (expected[i]-hot_one[i]) * LR

            for j in range(1, len(weights[i])): # bias calc sep
                weights[i][j] = change(weights[i][j],Xin[j-1],LR,expected[j]-hot_one[j])

def loss(Ycal, Yexp):
    summation = 0
    for i in range(len(Ycal)):
        summation += ( Ycal[i] - Yexp[i] ) ** 2

    return 1/2 * summation

def column(matrix, col):
    return [ a[col] for a in matrix ]

def scale(x, Max, Min):
    return ( x - Min ) / ( Max - Min )
