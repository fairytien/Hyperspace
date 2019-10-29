# Input a trio of any numbers and check if that trio makes up a right triangle.
# Raise ValueError if any of the input numbers is not integer or positive.

def right_triangle_errors(a, b, c):
    if isinstance(a, int) and isinstance(b, int) and isinstance(c, int):
        if a > 0 and b > 0 and c > 0:
            if a*a == b*b + c*c or b*b == c*c + a*a or c*c == a*a + b*b:
                return True
            else:
                return False
        else:
            raise ValueError("Incorrect value")
    else:
        raise ValueError("Incorrect value")
