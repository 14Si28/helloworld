import csv
with open("FileName.csv") as fn:
    fn_content= csv.reader(fn, delimiter=',') # If in your file delimiter is some other symbol, a pipe sign or any thing then you should put that symbol as a delimiter.
    print(fn_content)

    stock=[]
    price=[]

    for row in fn_content:
        stock.append(row[0])
        price.append(row[1])

    print(stock ,"\n", price)

# Now if we want to know the price of tht specific stock from out sheet then we work with the indexes.

stockname=input("Enter the name of the stock: ")
index_stock= stock.index(stockname.upper()) #Upper is done so we can capitilise the input text, as we know all the text is in capitals in csv.
print(price[index_stock])  
