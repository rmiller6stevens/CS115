#Robert Miller
#"I pledge my honor that I have abided by the Stevens Honor System."
def dotProduct(L,K):
#L and K are lists of numbers
    if L == [] or K == []:
        return 0.0
    return L[0] * K[0] + dotProduct(L[1:],K[1:])
def expand(S):
#S is a string, returns a list of the characters in string
    if S == '':
        return []
    return [S[0]] + expand(S[1:])
def deepMember(e, L):
# L is a list of values, and e is any value to find in L, returns True if found and False if not
    if not L:
        return False
    if isinstance(L[0],list):
        if True == deepMember(e, L[0]):
            return True
        else:
            return deepMember(e, L[1:])
    else:
        if e == L[0]:
            return True
        else:
            return deepMember(e, L[1:])
def removeAll(e, L):
#the value e is to be removed from the list of values, L
    if not L:
        return []
    if e == L[0]:
        return removeAll(e,L[1:])
    else:
        return [L[0]] + removeAll(e,L[1:])
def deepReverse(L):
#L is a list of values that needs to be reversed
    if not L:
        return []
    if isinstance(L[0],list):
            return deepReverse(L[1:]) + [deepReverse(L[0])]
    else:
        return deepReverse(L[1:]) + [L[0]]
    
