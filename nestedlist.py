if __name__ == '__main__':
    lst= [ ]
    a=int(input())
    for _ in range(a):
        name = input()
        score = float(input())
        lst.append([name,score]) 
    li2 = []
    for i in range(a):
        for j in range(a):
            k = lst[i][1]
        
        li2.append(k)
        
    li2.sort()
        
    z1 = set(li2)
    z2 = list(z1)
    z2.sort()
        
    x = z2[1]
    flist = []
    for i in lst:
        if x in i:    
            frep = lst[lst.index(i)][(i.index(x)-1)] 
            flist.append(frep)
    flist.sort()
    for i in flist:
        print(i)
