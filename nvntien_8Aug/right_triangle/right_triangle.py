def right_triangle(a, b, c):
    if a*a == b*b + c*c or b*b == a*a + c*c or c*c == a*a + b*b:
        return(True)
    else:
        return(False)
