def find_sum(lst,k):
  nlst=[]
  for num in lst:
    if k-num in lst:
      nlst.append(k-num)
      nlst.append(num)
  return nlst;

def find_sum_index(lst,k):
  nlst={}
  for i,n in lst:
    if k-num in nlst:
      return [nlst[k-num],i]
    nlst[n]=i
  
        
print(find_sum([1,21,3,14,5,60,7,6],81))
print(find_sum_index([1,21,3,14,5,60,7,6],81))
