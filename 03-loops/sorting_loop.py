srt = ['Rohan','Baiju','Raju','Rajshri','Aditya','Aradhya','Deepak','Vedansh','Siddartha']
x=[]
l=len(srt)
for i in range(l):
    swapped = False
    for j in range(l-1-i):
        if srt[j]>srt[j+1]:
            srt[j], srt[j+1] = srt[j+1], srt[j]
            swapped = True
    if not swapped:     
        break
print(srt)
