from collections import deque
 
def merge(X,Y):
    X, Y, Z = deque(X), deque(Y), []
    while len(X) > 0 and len(Y) > 0:
        if X[0] < Y[0]: Z.append( X.popleft() )
        else:           Z.append( Y.popleft() )
    return Z+list(X)+list(Y)
 
def bottom_up_mergesort(A):
    if len(A) <= 1: return list(A)
    Q = deque( [a] for a in A )
    while True:
        X = Q.popleft()
        if len(Q)==0: return X
        Y = Q.popleft()
        # try enabling this debug output:
        # print('merging',X,'and',Y)
        Q.append( merge(X,Y) )
 
print(bottom_up_mergesort('abracadabra'))
