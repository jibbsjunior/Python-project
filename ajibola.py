x=1
while(x<100):
    if(x%3==0 and x%5==0):
        print(x,"fizzbuzz")
    elif(x%3==0):
        print(x,"Fizz")
    elif(x%5==0):
        print(x,"Fizz")
    else:
        print(x)
    x+=1
