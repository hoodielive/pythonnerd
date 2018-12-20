def rangeToList(k):
    result = []
    for i in range(O,k):
        result.append(str(i))
    return result

def baseKStrings(n,k):
    if n == 0: return []
    if n == 1: return rangeToList(k)
    return  digit+bitstring for digit in baseKStrings(l,k)
                for bitstring in baseKStrings(n-l,k)

print(baseKStrings(4,3))
