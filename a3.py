def sumfun(num):
  list1=list(num)
  sum=0
  for x in list1:
     sum=sum+x
  return sum

n=(1,3,5,7,34,78,23)
print("Tuple is:",n)
print("Average of tuple is :",sumfun(n)/len(n))

