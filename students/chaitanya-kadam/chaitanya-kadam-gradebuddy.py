def avg(n1,n2,n3):
    a=n1+n2+n3/3
    return(a)

def result(a):
    if a>=75:
        return("distiction")
    elif a>=35:
        return("pass")
    else:
        return("fail")

def classify_grade(a):
    if a >= 90:
        return("A")
    elif a >= 80:
        return("B")
    elif a >= 70:
        return("C")
    elif a >= 60:
        return("D")
    else:
        return("F")
