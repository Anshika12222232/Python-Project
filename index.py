n=int(input("Enter the no of cuts:"))
p=n*2
if 360%p==0:
    print("cake can be cut in %d equal parts"%p)
else:
    print("cake can not be cut in %d equal parts"%p)    
if p<360:
    print("cake can be cut in %d parts"%p)
else:
    print("cake can not  be cut in %d parts"%p)    
if  (p * (p + 1)) / 2 <= 360:
    print("Cake can be cut into %d parts such that no two of them are equal"%p)  
else:
    print("Cake can not  be cut into %d parts such that no two of them are equal"%p)
