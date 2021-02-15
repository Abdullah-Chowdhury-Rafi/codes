def raf():
    r=int(input())
    s=list(map(int,input().split()))
    j=s[0]+s[1]
    if s[r-1]>=j: print(1,2,r)
    else: print(-1)
def main():
    t=int(input())
    while t: raf();t-=1
if __name__=='__main__':
    main()
