class Car:
    def details(self,model,make):
        self.model=model
        self.make=make
    def showDetails(self):
        print(f"Model Number : {self.model}")
        print(f"Make In : {self.make}")
        

obj = Car()
obj.details("2002","Wood")
obj.showDetails()   
print(Car.__dict__)     
        