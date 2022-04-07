class supermarket:
    def __init__(self,product_name,item1,item2):
        self.product_name = product_name
        self.item1 = item1
        self.item1 = item1
    def getdetails(self):
        self.product_name = input("enter the product name")
        self.item1 = input("enter the item 1")
        self.item2 = input("enter the item 2")
    def putdetails(self):
        print(self.product_name,self.item1,self.item1)

class billing(supermarket):
    #def __init__(self,billno):
        #self.billno = billno
    def inputdetails(self):
        self.billno = int(input("enter the billno"))
    def putdetails1(self):
        print(self.billno)

obj = billing('','','')
obj.getdetails()
obj.putdetails()
obj.inputdetails()
obj.putdetails1()
obj.putdetails()



