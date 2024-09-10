mwr=[{'dress':'Shirt','id':100,'stock':15,'price':1500},{'dress':'Jeans','id':101,'stock':20,'price':2500},{'dress':'Tshirt','id':102,'stock':25,'price':1000}]
while True:
    print('''
          1.Dress Details
          2.view the Dress Details
          3.Update the Dress Details
          4.Delete the Dress Details
          5.Search the Dress Details  
          6.exit''')
    choice=int(input('enter the choice:'))
    if choice==1:
        dress=str(input('enter the dress:'))
        id=int(input('enter the id:'))
        price=int(input('enter the price:'))
        stock=int(input('enter the available stock:'))
        mwr.append({'dress':dress,'id':id,'stock':stock,'price':price})
    elif choice==2:
        for i in mwr:
            print(i)
    elif choice==3:
        id=int(input('enter the id:'))
        f=0
        for i in mwr:
            if id==i['id']:
                while True:
                    print('''
                          1.Update dress
                          2.Update stock
                          3.Update price
                          4.exit''')

                    choice=int(input('enter the choice:'))

                    if choice==1:
                        dress=str(input('enter the dress:'))
                        i['dress']=dress
                    elif choice==2:
                        stock=int(input('enter the stock:'))
                        i['stock']=stock
                    elif choice==3:
                        price=int(input('enter the price:'))
                        i['price']=price
                    elif choice==4:
                        break
                    else:
                        print('invalid choice')
                    f=1
        if f==0:
            print('invalid id')
    elif choice==4:
        id=int(input('enter the id:'))
        f=0
        for i in mwr:
            if id==i['id']:
                mwr.remove(i)
                f=1
        if f==0:
            print('invalid id')
    elif choice==5:
        id=int(input('enter the id:'))
        f=0
        for i in mwr:
            if id==i['id']:
                print(i)
                f=1
        if f==0:
            print('invalid id')
    elif choice==6:
        break
    else:
        print('invalid choice')