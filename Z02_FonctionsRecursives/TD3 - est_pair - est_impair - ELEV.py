def est_pair(n):
    if n == 0:
        return True
    return est_impair(n-1)

def est_impair(n):
    if n == 0:
        return False
    return est_pair(n-1)




def tests():
    for n in range(20):
        for parity,func in enumerate((est_pair, est_impair)):
            actual   = func(n)
            expected = n%2 == parity
            assert actual==expected, "{}({}): {} should be {}".format(func.__name__, n, actual, expected)
    else:
        print('ok!')

tests()