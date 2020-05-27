SOLUTION 1

def solution(number):
  result=[]
  for i in range(1, number):
      if i%3==0 or i%5==0:
        result.append(i)
  return sum(result)
  
  SOLUTION 2
  
  def solution(number):
    return sum(x for x in range(number) if x%3==0 or x%5==0)
