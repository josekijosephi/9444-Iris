from mathematical import sigmoid
from numpy import matmul, argmax, array

def forwardPass (Xin, weights):
    output = sigmoid(matmul(Xin, weights))

    aMax = argmax(output)
    hot_one = [ (aMax == 0),  (aMax == 1), (aMax == 2) ]
    #tol = 0.5
    #hot_one = [ x > tol for x in output ]

    return output, array(hot_one)
