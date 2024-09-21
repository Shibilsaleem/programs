def maxArea(lengths):
    finalsticks=set()
    area=float('-inf')
    for stick in lengths:
        if lengths.count(stick)>=2:
            finalsticks.add(stick)
    new=list(finalsticks)
    for i in range(len(new)-1):
        for j in range(i+1,len(new)):
            if new[i]*new[j]>area:
                area=new[i]*new[j]
    return area
sticks=list(map(int,input('Enter the length of sticks : ').split()))
print(maxArea(sticks))