#Price with value added tax program
name = "Mercedes W177"
net = 29999.9
tax = 17
gross = net*tax/100
out = name +"\t"+"price\t"+str(gross)
print(out)
