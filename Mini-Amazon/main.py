from Auth import *
from dup_product import Product
from Billing import Bill
class Store():
    def __init__(self) -> None:
        print("""▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█░███░█░▄▄█░██▀▄▀█▀▄▄▀█░▄▀▄░█░▄▄███▄░▄█▀▄▄▀███░▄▀▄░█░██░███░▄▄█▄░▄█▀▄▄▀█░▄▄▀█░▄▄
█▄▀░▀▄█░▄▄█░██░█▀█░██░█░█▄█░█░▄▄████░██░██░███░█▄█░█░▀▀░███▄▄▀██░██░██░█░▀▀▄█░▄▄
██▄█▄██▄▄▄█▄▄██▄███▄▄██▄███▄█▄▄▄████▄███▄▄████▄███▄█▀▀▀▄███▄▄▄██▄███▄▄██▄█▄▄█▄▄▄
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
▀▀

""")
obj=Store()
ob=Auth()
ob.registration()
ob.login()
ob1 =Product()
ob1.display()
ob1.purchase()
bill=Bill()
bill.form()

