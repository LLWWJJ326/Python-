SYC=[]
for i in range(1,10):
    for j in range(10):
        for k in range(10):
            for h in range(10):
                if i**4 + j**4 + k**4 + h**4 == 1000*i + 100*j + 10*k + h:
                    SYC.append(1000*i + 100*j + 10*k + h)
print(SYC)

