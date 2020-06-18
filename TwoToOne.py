Take 2 strings s1 and s2 including only letters from ato z. 
Return a new sorted string, the longest possible, containing distinct letters,

each taken only once - coming from s1 or s2.  

SOLUTION 1

def longest(s1, s2):
    return "".join(sorted(set(s1+s2)))
    
SOLUTION 2

def longest(s1, s2):
    result=[]
    for records in s1:
        if records not in result:
           result.append(records)
    for records in s2:
        if records not in result:
            result.append(records)
    result=sorted(result)
