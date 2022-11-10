# Créer une fonction prenant 4 paramètres et les retournant en ordre croissant en utilisant que des conditions(en n’utilisant pas de loops).

def triage (n1, n2, n3, n4):

    min_v = min(n1, n2, n3, n4)
    max_v = max(n1, n2, n3, n4)
    
    if n1 == min_v:
        if n2 == max_v:
            if n3 <= n4:
                return n1, n3, n4, n2 
            else:
                return n1, n4, n3, n2
        elif n3 == max_v:
            if n2 <= n4:
                return n1, n2, n4, n3
            else:
                return n1, n4, n2, n3
        elif n4 == max_v:
            if n2 < n3:
                return n1, n2, n3, n4
            else:
                return n1, n3, n2, n4

    if n2 == min_v:
        if n1 == max_v:
            if n3 <= n4:
                return n2, n3, n4, n1 
            else:
                return n2, n4, n3, n1
        elif n3 == max_v:
            if n1 <= n4:
                return n2, n1, n4, n3
            else:
                return n2, n4, n1, n3
        elif n4 == max_v:
            if n1 < n3:
                return n2, n1, n3, n4
            else:
                return n2, n3, n1, n4 

    if n3 == min_v:
        if n1 == max_v:
            if n2 <= n4:
                return n3, n2, n4, n1
            else:
                return n3, n4, n2, n1
        elif n2 == max_v:
            if n1 <= n4:
                return n3, n1, n4, n2
            else:
                return n3, n4, n1, n2
        elif n4 == max_v:
            if n1 < n2:
                return n3, n1, n2, n4
            else:
                return n3, n2, n1, n4 

    if n4 == min_v:
        if n1 == max_v:
            if n2 <= n3:
                return n4, n2, n3, n1 
            else:
                return n4, n3, n2, n1
        elif n2 == max_v:
            if n1 <= n3:
                return n4, n1, n3, n2
            else:
                return n4, n3, n1, n2
        elif n3 == max_v:
            if n1 < n2:
                return n4, n1, n2, n3
            else:
                return n4, n2, n1, n3

a, b, c, d = 15, 19, 24, 7

print(triage(a, b, c, d))
