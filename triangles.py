def triangleByHeight(height):
    for i in range(1,height+1):
        line=i*"*"
        l=len(line)
        while(l<height):
            line=" "+line
            l+=1
        line+=(i-1)*"*"
        print(line)
def triangleByBase(base):
    tablen=base 
    for i in range(1,base+1,2):
        line=" "*tablen
        tablen-=1
        line+=i*"*"
        print(line)

