# WAPP to implement queue operation 
l=[]
for i in range(100):
    print("1.push")
    print("2.pop")
    print("3.display")
    print("4.exit")
    x=int(input("selct a option:"))
    if x==1:
        j=int(input("push elements"))
        l.append(j)
        print("list",l)
    elif x==2 :
        l.remove(k)
        print("list=",l)
    elif x==3:
        print("list",l)
    elif x==4:
        print("exit")
        break
    else:
        print("choose correct option")
    n=len(l)
    k=l[0]

