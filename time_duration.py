def add_time(start,duration):
    #duration='32 : 56'
    #start='3:30 am'
    #mak tuple second param and convert duration number to integer 
    tuple_duration=duration.partition(':')
    hour=int(tuple_duration[0])
    colen=tuple_duration[1]
    minuten=int(tuple_duration[2])

    ##mak tuple first param and convert duration number to integer 
    tuple_start=start.split()
    xx=tuple_start.remove(tuple_start[1])
    h_c_m=tuple_start[0].partition(':')
    hour1=int(h_c_m[0])
    colen1=h_c_m[1]#print(hour1)
    minuten1=int(h_c_m[2])
    #print(minuten1)
     

    adi_h=hour1+hour
    adi_m=minuten1+minuten

    am_pm=''
    if adi_h>12:
        am_pm='PM'
    else:am_pm='AM' 
    print(adi_h,colen1,adi_m,'',am_pm)
    return add_time
