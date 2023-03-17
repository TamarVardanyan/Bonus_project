import time
try:
    my_time=input("Insert time to count down (h:m:s) ")
    list_time=list(my_time.split(':'))
    h=int(list_time[0])
    m=int(list_time[1])
    s=int(list_time[2]) 
    second=h*3600+m*60+s
    def clock(x):
        if h<24 and m<60 and s<60:
            for x in range(second, -1, -1):
                seconds=x%60 
                minute=int(x/60)%60
                hour=int(x/3600)%24
                print(f"{hour:02}:{minute:02}:{seconds:02}")
                time.sleep(1)
        elif h>23:
            print("Hours can't be more than 23")
        elif m>59:
            print("Minutes can't be more than 59")
        else:
            print("Seconds can't be more than 59")
    clock(second)
except:
    print('Try again')