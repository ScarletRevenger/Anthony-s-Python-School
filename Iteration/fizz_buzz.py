for i in range(1,21):
    # print(i)
    d3 = False
    d5 = False

    if i % 3 == 0:
        d3 = True

    if i % 5 == 0:
        d5 = True
    
    if d3 is True and d5 is not True:
        print("fizz")
    
    if d3 is not True and d5 is True:
        print("buzz")
    
    if d3 is True and d5 is True:
        print("fizz buzz")
    
    if d3 is not True and d5 is not True:
        print(i)