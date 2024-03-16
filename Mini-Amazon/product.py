import csv
class product:
    def __init__(self):
        pass
    def display(self):
        with open("products.csv","r",newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                print(row["product"],"->","Rs.",row["price"])
        
    def purchase(self):
        self.item =input("Enter the product name:")
        with open("products.csv","a",newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if (row["product"]==self.item and int(row['quantity'])>0):
                    val =int(row['quantity'])
                    no=int(input("Enter the number of item want to buy:"))
                    if((val-no)>0):
                        row['quantity']=val-no
                        # writer = csv.writer(f)
                        # writer.writerow([i for i in row.values()])
                        print("You have successfully bought",no)
                    else:
                        print("Out of stock")
                else:
                    print("Item not available  or spelled wrongly.")
                    
        # if item not in self.items:
        #     return "Item is not available."
        # else:
        #     count=int(input("Enter the number of "+item+" you want to buy :"))
        #     if count>self.items[item]:
        #         return "We are out of stock"
        #     else:
        #         self.items[item] -=count
                
ob=product()
ob.display()
ob.purchase()
