import csv

class Product:
    def __init__(self):
        print("*****************************Welcome to the product pages************************************")
        print()
        self.item=""
    def display(self):
        with open("products.csv","r",newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                print(row["product"],"->","Rs.",row["price"], "-> Quantity:", row["quantity"])
                print()
    def purchase(self):
        self.item = input("Enter the product name: ")
        with open("products.csv","r",newline="") as f:
            reader = csv.DictReader(f)
            products = list(reader)  # Convert reader to list to reset file pointer
        found = False
        for row in products:
            if row["product"] == self.item and int(row['quantity']) > 0:
                found = True
                val = int(row['quantity'])
                no = int(input("Enter the number of ❤️  items you want to buy: "))
                if val - no >= 0:
                    row['quantity'] = str(val - no)  # Update quantity
                    with open("products.csv", "w", newline="") as f:
                        writer = csv.DictWriter(f, fieldnames=reader.fieldnames)
                        writer.writeheader()
                        writer.writerows(products)  # Rewrite entire file with updated quantities
                    print("🎉🎉You have successfully bought ", no, "of", self.item,"🎖️🎖️")
                    print("Total amount is ",no*int(row['price']))
                    print("Kindly pay on delivery")
                else:
                    print("Out of stock")
                break
        if not found:
            print("Item not available or spelled wrongly.")
            ob=Product()
            ob.purchase()

# ob = Product()
# ob.display()
# ob.purchase()
