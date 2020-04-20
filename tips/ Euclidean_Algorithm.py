def euclidean(p, q):
    if p < q:
        p, q = q, p
    while(1):
        if p % q == 0:
            return q
        p, q = q, p % q
