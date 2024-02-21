class product():
    def __init__(self,code,name,supplier,price):
        self.code=code
        self.name=name
        self.supplier=supplier
        self.price=price
    def information(self):
        return f"code:{self.code} name:{self.name} supplier:{self.supplier} price:{self.price}"
laptop=product(1,"HP LAPTOP","HP",70000)
info=laptop.information()

print(info)

car=product(0,"AUDI XS","AUDI",12000000)
info=car.information()
print(info)