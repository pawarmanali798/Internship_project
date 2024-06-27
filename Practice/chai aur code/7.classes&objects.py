class Car:
    def __init__(self,brand,model):
        self.__brand=brand
        self.model=model

    
    def fullname(self):
        return f"{self.__brand} {self.model}"
    
    def get_brand(self):
        return f"{self.__brand}--{self.model}"
        
objCar=Car("tesla","model S")
print(objCar.get_brand())
print(objCar.__brand())


# class Electricar(Car):
#     def __init__(self,brand,model,battery_size):
#         super().__init__(brand,model)
#         self.battery_size=battery_size

# electri_obj=Electricar("tesla","Model S","85kWh")
# print(electri_obj.fullname())

# myobjCar=Car("Toyota","Safari")
# print(myobjCar.brand)
# print(myobjCar.model)

# newobjCar=Car("ranault","jaguar")
# print(newobjCar.model)

# formobj=Car("Maruti","suzuki")
# print(formobj.fullname())
# print(formobj.lname)




    