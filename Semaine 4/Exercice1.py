def triage (n1, n2, n3, n4):

    min_v = min(n1, n2, n3, n4)
    max_v = max(n1, n2, n3, n4)
    
    if n1 == min_v:
        if n2 == max_v:
            if n3 <= n4:
                return n1, n3, n4, n2 
            else:
                return n1, n4, n3, n2
        else:
            if n3 == max_v:
                if n2 <= n4:
                    return n1, n2, n4, n3 
                else:
                    return n1, n4, n2, n3
            else:
                if n4 == max_v:
                    
