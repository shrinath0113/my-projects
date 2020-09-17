def sort(vals):
    for i in range(len(vals)-1,0,-1):
        for j in range(i):
            if vals[j]>vals[j+1]:
                temp=vals[j]
                vals[j]=vals[j+1]
                vals[j+1]=temp


vals=[7,4,6,1,54,24,243]
sort(vals)

print(vals)