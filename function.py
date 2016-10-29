import time

a = time.localtime(time.time())
def asctFunction(a):
    print(a.tm_wday," ",a.tm_mday," ",a.tm_hour," ",a.tm_min," ",a.tm_sec," ",a.tm_year)
    return;

#asctFunction(a)

def printf(*variable):
    for var in variable:
        print(var)
    return

#printf(10, 12, 23, 89, 90, 12)

sum = lambda a1, a2: a1 + a2;

#print(sum(10, 10));

