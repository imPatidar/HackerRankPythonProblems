#for matrix with length 3X3

arr=[[1,2,3],[1,2,3],[1,2,3]]
d1=sum(arr[i][i] for i in range(len(arr)))
d2=sum(arr[i][3-i-1] for i in range(len(arr)))

print(d1,d2)