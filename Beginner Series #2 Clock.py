SOLUTION 1

def past(h, m, s):
    return (3600*h + 60*m + s) * 1000
    
SOLUTION 2

def past(h, m, s):
    h=h*3600000
    m=m*60000
    s=s*1000
    return float(h+m+s)
