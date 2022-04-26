def magic_square(matrix):
   size=len(matrix[0])
   sum_list=[]
   for col in range(size): #Verti sum
       sum_list.append(sum(row[col] for row in matrix))
   sum_list.extend([sum(lines) for lines in matrix])#Horizon sum
   result1=0
   for i in range(0,size):
       result1+=matrix[i][i]
   sum_list.append(result1)
   result2=0
   for i in range(size-1,-1,-1):
       result2+=matrix[i][i]
   sum_list.append(result2)
   if len(set(sum_list))>1:
       return False
   return True