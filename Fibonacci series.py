def series(n):
        f=0
        s=1
        while f<=n:
                print(f)
                t=f+s
                f=s
                s=t
num=input("Enter a number: ")
series(int(num))
