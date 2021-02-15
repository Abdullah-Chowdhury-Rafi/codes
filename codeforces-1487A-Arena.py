def raf():
    r=int(input())
    s=list(map(int,input().split()))
    s.sort()
    i=0
    while i<len(s)-1:
        if s[i]!=s[i+1]: print(len(s)-i-1);return
        i+=1
    print(0)
def main():
    t=int(input())
    while t: raf();t-=1
if __name__=='__main__':
    main()
 
