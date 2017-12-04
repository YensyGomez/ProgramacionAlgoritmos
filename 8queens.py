reinas = 8
solution = 3
def validarReina(R,reinas):
    for i in range(reinas):
        for j in range(reinas):
            if (i != j):
                if(abs(i - j) == abs(R[i] - R[j])):
                    return False
                if (R[i] == R[j]):
                    return False
    return True

def combinatoria(reinas,solution):
    for a in range(reinas):
        for b in range(reinas):
            for c in range(reinas):
                for d in range(reinas):
                    for e in range(reinas):
                        for f in range(reinas):
                            for g in range(reinas):
                                for h in range(reinas):
                                    v = [a, b, c, d, e, f, g, h]
                                    validar = validarReina(v,reinas)
                                    if validar == True:
                                        solution = solution - 1
                                        print v
                                        if solution == 0:
                                            return 0

print combinatoria(reinas, solution)
