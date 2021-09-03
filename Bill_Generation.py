from datetime import datetime

name= input("Enter the name: ")
#Lists of Items
lists='''
Denim Jeans  Rs 800
Roadster     Rs 450
Levis        Rs 600
Polo         Rs 900
HRX          Rs 720
Rabbit       Rs 1110
Wrogn        Rs 650
Highlander   Rs 840

'''

price=0
pricelist=[]
totalprice=0
Finalfinalprice=0
ilist=[]
qlist=[]
plist=[]

#rates of Items

items={
    'Denim Jeans':800,
    'Roadster':450,
    'Levis':600,
    'Polo':900,
    'HRX':720,
    'Rabbit':1110,
    'Wrogn':650,
    'Highlander':840
}
option=int(input("For displaying the Brands press 1: "))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("If you want buy press1 or 2 for Exit: "))
    if inp1==2:
        break
    if inp1==1:
        item=input("Enter your Item:")
        quantity=int(input("Enter Quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("Out Of Stock")    
    else:
        print("you entered wrong number")
    inp=input("can I bill the Items, yes or no: ")
    if inp=='yes':
        pass
        if finalamount!=0:
            print(25*"=","Trendz",25*"=")
            print(28*" ","Hyderabad")
            print("Name:",name,30*" ","Date:",datetime.now())
            print(75*"-")
            print("sno",8*" ",'items',8*" ",'Quantity',3*" ",'price')
            for i in range(len(pricelist)):
                print(i,8*' ',5*' ',ilist[i],3*' ',qlist[i],8*" ",plist[i])
            print(75*"-")
            print(50*" ",'TotalAmount:','Rs',totalprice)
            print("gst amount",40*" ",'Rs',gst)
            print(75*"-")
            print(50*" ",'finalamount:','rs',finalamount)
            print(75*"-")     
            print(20*" ","Thanks For Visiting")
            print(75*"-")