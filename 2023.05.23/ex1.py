monthlyIncome=int(input("Enter Your Income:-"))

anual=12*monthlyIncome

rate=[0.06,0.08,0.012,0.018,0.024,0.032,0.036]

slab=[]

if(anual>=1200000):
    slot=0
    taxableIncome= anual - 1200000
    reminder=taxableIncome % 500000
    balence = taxableIncome - reminder
    slot=balence /500000

    if(reminder>0):
        slot=slot+1

    if(slot>6):
        slot=6
    
    dadicateAmount=taxableIncome
    for i in range(1,int(slot)):
        slab.append(500000)
        dadicateAmount=dadicateAmount-500000
    slab.append(dadicateAmount)

    tax=0

    for j in range(0,len(slab)):
        tax=tax+(slab[j]*rate[j])

    taxMonth= tax/12

    print("your mothly Tax Amunt is:", taxMonth)
    print("Your yearly tax amunt is:",tax)

else:
    print("your not pay for tax:")
