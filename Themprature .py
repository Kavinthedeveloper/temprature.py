c=float(input("enter degree in celcios"))
f=(c*1.8)+32
print(c,"dregree in celcious is = to ",f ,"in fahrenhet")

print("%0.1f degree is equal to %0.1f if degree fahrenhet"%(c,f))

if f>=104:
    print("the temprature is to hot")
elif f<=50:
    print ("It to cold")
else :
    print ("its nice weather")

    