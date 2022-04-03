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
    def details(self):
        print(self.billno)


class billing1(billing):
    #def __init__(self,billno):
        #self.billno = billno
    def inputdetails1(self):
        self.billno = int(input("enter the billno"))
    def details1(self):
        print(self.billno)


class billing2(billing1):
    #def __init__(self,billno):
        #self.billno = billno
    def inputdetails2(self):
        self.billno = int(input("enter the billno"))
    def details2(self):
        print(self.billno)
        

obj = billing2('','','')

obj.getdetails()
obj.putdetails()
obj.inputdetails()
obj.details()
obj.inputdetails1()
obj.details1()
obj.inputdetails2()
obj.details2()
obj.putdetails()


