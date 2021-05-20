def solution(x, n):
      if x >= 0: 
        return [i for i in range(x, x*n+1 ,x)]
    elif x == 0 :
        return [0]
    else :
        X = abs(x)
        return [ i*(-1) for i in range(X, X*n+1, X)]
solution(-4,2)