import csv
with open('FileName.CSV') as fn:
    file_content=csv.reader(fn,delimiter=',')
    print(file_content)

    stock=[]
    price=[]
    for i in file_content:
        stock.append(i[0])
        price.append(i[1])

    print(stock,"\n",price)

    try:
        stockname= input("Enter the name of the stock: ")
        st_index= stock.index(stockname.upper())
        print(price[st_index])

    except Exception:
        print("Try again invalid value")
