
def mergeSort(arr,temp, val1 = None, val2 = None, i = None,j = None,indx = None,temp_val=[None,0]):
  if len(arr) <= 1:
    return arr

  else:
      mid = len(arr) // 2
      a1 = mergeSort(arr[:mid],temp,val1, val2, i,j,indx,temp_val)
      if len(a1) > 1:
        val1 = a1[0]
        val2 = a1[1]
        i = a1[2]
        j = a1[3]
        indx = a1[4]
        temp_val = a1[6]
      elif len(a1) == 1 and indx == None:
        indx = 0
      elif len(a1) == 1 and indx != None:
        indx += 1
      a2 = mergeSort(arr[mid:], temp, val1,val2, i,j,indx,temp_val)  
      if len(a2) > 1:

        val1 = a2[0]
        val2 = a2[1]
        i = a2[2]
        j = a2[3]
        indx = a2[4]
      elif len(a2) == 1 and indx != None:
        indx += 1
      if len(a1) == 1 and len(a2) == 1:
        if i == None and j == None:
          i = 0
          j = 1
          sum = None
          return (a1[0],a2[0],i,j,indx,sum,temp_val)
        elif (val2**2) <= (a1[0]**2):
          if val1 < val2:
            val1 = val2
            i = j
          val2 = a1[0]
          j = indx -1 
        elif (val2**2) <= (a2[0]**2):
          if val1 < val2:
            val1 = val2
            i = j
          val2 = a2[0]
          i = indx
        if temp_val[1] < j and temp_val[0] != None and val1 < temp_val[0]:
          val1 = temp_val[0]
        if val1 < a1[0] and (indx -1 < j):
          val1 = a1[0]
          i = indx -1
        elif val1 < a1[0] and (indx -1 > j):
          temp_val[0] = a1[0]
          temp_val[1]=indx-1
        elif val1 < a2[0] and (indx < j):
          val1 = a2[0]
          i = indx
        elif val1 < a2[0] and (indx > j):
          temp_val[0]=a2[0]
          temp_val[1]=indx


      if len(temp)-1 == indx:
        if j > temp_val[1] and temp_val[0]!=None and val1 < temp_val[0]:
          val1 = temp_val[0]
      sum = val1 + (val2 ** 2)
      return (val1,val2,i,j,indx,sum,temp_val)



input = open("input4.txt", "r")
output = open("output4.txt", "w")

n1 = input.readline().split()
arr1 = list(map(int,input.readline().split()))

a = mergeSort(arr1,arr1)
output.write(str(a[5]))
